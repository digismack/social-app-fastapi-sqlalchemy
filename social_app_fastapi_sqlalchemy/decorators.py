from functools import wraps

from .utils import load_backend, load_strategy


def psa(redirect_uri=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, backend, *args, **kwargs):
            uri = redirect_uri
            if uri and not uri.startswith("/"):
                uri = url_for(uri, backend=backend)
            self.strategy = load_strategy()
            self.backend = load_backend(self.strategy, backend, redirect_uri=uri, *args, **kwargs)
            return func(backend, *args, **kwargs)

        return wrapper

    return decorator
