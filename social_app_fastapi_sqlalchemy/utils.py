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


def reverse(route: str, **kwargs) -> URLPath:
    from app.routers.assignment import router as assign_router
    from app.routers.game import router as game_router
    from app.routers.talks import router as talk_router
    from app.routers.topics import router as topic_router

    ALL_ROUTERS = [assign_router, topic_router, game_router, talk_router]

    for router in ALL_ROUTERS:
        try:
            path = router.url_path_for(route, **kwargs)
            return path
        except NoMatchFound:
            pass

    raise Exception(f"No url path could be found for {route}")
