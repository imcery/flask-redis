# Flask-Redis

Adds Redis support to Flask. Built on top of [redis-py][1].

## Installation

```
pip install git+https://github.com/imcery/flask-redis#egg=flask-redis
```

Or if you use pipenv

```
pipenv install git+https://github.com/imcery/flask-redis#egg=flask-redis
```

## Configuration

Your configuration should be declared within your Flask config. Set the URL of
your database like this:


```python
    REDIS_URL = "redis://:password@localhost:6379/0"
    # or
    REDIS_URL = "unix://[:password]@/path/to/socket.sock?db=0"
```

To create the redis instance within your application:

```python
    from flask import Flask
    from flask_redis import Redis

    app = Flask(__name__)
    redis_store = Redis(app)
```

or

```python
    from flask import Flask
    from flask_redis import Redis

    redis_store = Redis()

    def create_app():
        app = Flask(__name__)
        redis.init_app(app)
        return app
```

or maybe you want to use [mockredis](https://github.com/locationlabs/mockredis)
to make your unit tests simpler.

```python
    from flask import Flask
    from flask_redis import Redis

    app = Flask(__name__)
    app.config['REDIS_CONNECTION_CLASS'] = 'mockredis.MockRedis'

    redis_store = Redis(app)
```

## Usage

`Flask-Redis` proxies attribute access to an underlying Redis connection. So
treat it as if it were a regular `Redis` instance.

```python
    from extensions import redis_store

    @app.route('/')
    def index():
        return redis_store.get('prefix:key')
```

**Protip:** The [redis-py][1] package currently holds the 'redis' namespace, so
if you are looking to make use of it, your Redis object shouldn't be named 'redis'.

For detailed instructions regarding the usage of the client, check the
[redis-py][1] documentation.

Advanced features, such as Lua scripting, pipelines and callbacks are detailed
within the [redis-py][1] README.

[1]: https://github.com/andymccurdy/redis-py
