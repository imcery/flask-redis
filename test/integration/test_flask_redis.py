"""Integration tests for Flask-Redis."""

import flask
import pytest
import redis as rd

from flask_redis import Redis


@pytest.fixture
def app():
    return flask.Flask(__name__)


def test_constructor(app):
    """Test that a constructor with app instance will initialize the
    connection.
    """
    redis = Redis(app)
    assert redis.client is not None
    assert hasattr(redis.client, 'connection_pool')


def test_init_app(app):
    """Test that a constructor without app instance will not initialize the
    connection.

    After Redis.init_app(app) is called, the connection will be initialized.
    """
    redis = Redis()
    assert redis.client is None

    redis.init_app(app)
    assert redis.client is not None
    assert hasattr(redis.client, 'connection_pool')

    if hasattr(app, 'extensions'):
        assert 'redis' in app.extensions
        assert app.extensions['redis'] == redis


def test_custom_prefix(app):
    """Test that config prefixes enable distinct connections."""
    app.config['REDIS_URL'] = 'redis://localhost:6379/1'
    redis_a = Redis(app)

    app.config['REDIS_URL'] = 'redis://localhost:6379/2'
    redis_b = Redis(app)

    assert redis_a.connection_pool.connection_kwargs['db'] == 1
    assert redis_b.connection_pool.connection_kwargs['db'] == 2


def test_custom_connection_class_using_string(app):
    """Test that Redis can be instructed to use a different Redis client
    using a class reference"""
    app.config['REDIS_CONNECTION_CLASS'] = 'redis.StrictRedis'

    redis = Redis()
    assert redis.client is None

    redis.init_app(app)
    assert redis.client is not None
    assert isinstance(redis.client, rd.StrictRedis)


def test_custom_connection_class_using_class(app):
    """Test that Redis can be instructed to use a different Redis client
    using a class reference"""
    class FakeProvider(object):

        @classmethod
        def from_url(cls, *args, **kwargs):
            return cls()

    app.config['REDIS_CONNECTION_CLASS'] = FakeProvider

    redis = Redis()
    assert redis.client is None

    redis.init_app(app)
    assert redis.client is not None
    assert isinstance(redis.client, FakeProvider)
