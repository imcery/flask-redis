from flask_redis import Redis


def test_constructor_app(mocker):
    """Test that the constructor passes the app to Redis.init_app"""
    mocker.patch.object(Redis, 'init_app', autospec=True)
    app_stub = mocker.stub(name='app_stub')

    Redis(app_stub)

    Redis.init_app.assert_called_once_with(mocker.ANY, app_stub)
