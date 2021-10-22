from social_core.utils import get_strategy, module_member
from starlette.datastructures import URLPath
from starlette.routing import NoMatchFound

DEFAULTS = {
    "STRATEGY": "social_app_fastapi_sqlalchemy.strategy.FastAPIStrategy",
    "STORAGE": "social_app_fastapi_sqlalchemy.storage.FastAPIStorage",
}


def do_login(backend, user, social_user):
    print('do_login backend', backend)
    print('do_login user', user)
    print('do_login social_user', social_user)
    return login_user(user)


def load_strategy(request):
    return get_strategy(DEFAULTS.get("STRATEGY"), DEFAULTS.get("STORAGE"), request)


def load_backend(strategy, name, redirect_uri):
    Backend = module_member(name)
    return Backend(strategy, redirect_uri)
