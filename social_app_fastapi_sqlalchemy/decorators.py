from functools import wraps

from .utils import load_backend, load_strategy


def psa(redirect_uri=None):
    def decorator(func):
        @wraps(func)
        def wrapper(request, backend, *args, **kwargs):
            uri = redirect_uri
            if uri and not uri.startswith("/"):
                uri = request.app.url_path_for(uri, backend=backend)
            strategy = load_strategy(request)
            request.strategy = strategy
            backend = load_backend(strategy, backend, redirect_uri=uri, *args, **kwargs)
            return func(request, backend, *args, **kwargs)

        return wrapper

    return decorator
