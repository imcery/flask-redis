import importlib

__all__ = ['Redis']
__version__ = '0.1'


class Redis(object):

    # The DSN (URL) of the Redis connection
    redis_url = 'redis://localhost:6379/0'

    # The Redis client class to use
    connection_class = 'redis.Redis'

    def __init__(self, app=None, **kwargs):
        self.client = None
        self.client_kwargs = kwargs

        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):
        self.redis_url = app.config.setdefault(
            'REDIS_URL',
            self.redis_url,
        )
        self.connection_class = app.config.setdefault(
            'REDIS_CONNECTION_CLASS',
            self.connection_class,
        )

        # Update client arguments
        self.client_kwargs.update(kwargs)

        # Dynamically import connection class from a string
        if isinstance(self.connection_class, str):
            module_name, attribute = self.connection_class.rsplit('.', 1)
            module = importlib.import_module(module_name)
            connection_class = getattr(module, attribute)
        else:
            connection_class = self.connection_class

        self.client = connection_class.from_url(
            self.redis_url, **self.client_kwargs)

        # Register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['redis'] = self

    def __getattr__(self, name):
        return getattr(self.client, name)

    def __getitem__(self, name):
        return self.client[name]

    def __setitem__(self, name, value):
        self.client[name] = value

    def __delitem__(self, name):
        del self.client[name]
