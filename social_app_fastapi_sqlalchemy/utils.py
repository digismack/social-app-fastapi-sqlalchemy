from social_core.utils import get_strategy, module_member
from starlette.datastructures import URLPath
from starlette.routing import NoMatchFound

DEFAULTS = {
    "STRATEGY": "social_app_fastapi_sqlalchemy.strategy.FastAPIStrategy",
    "STORAGE": "social_app_fastapi_sqlalchemy.storage.FastAPIStorage",
}


def do_login(backend, user, social_user):
    name = backend.strategy.setting("REMEMBER_SESSION_NAME", "keep")
    remember = (
        backend.strategy.session_get(name)
        or request.cookies.get(name)
        or request.args.get(name)
        or request.form.get(name)
        or False
    )

    return login_user(user, remember=remember)


def load_strategy(request):
    return get_strategy(DEFAULTS.get("STRATEGY"), DEFAULTS.get("STORAGE"), request)


def load_backend(strategy, name, redirect_uri):
    Backend = module_member(name)
    return Backend(strategy, redirect_uri)
