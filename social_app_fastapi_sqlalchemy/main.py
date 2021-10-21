import uvicorn
from fastapi import FastAPI, Response
from social_core.actions import do_auth, do_complete
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware

from .decorators import psa
from .utils import do_login, load_backend, load_strategy


app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="some-random-string")


@app.get("/", name="root_get")
@app.post("/", name="root_post")
async def root(request: Request):
    return {"message": "Hello World"}


@app.get("/auth/login/{backend}/", name="auth_login_get")
@app.post("/auth/login/{backend}/", name="auth_login_post")
@psa("complete")
async def auth_login(backend: str, request: Request):
    return do_auth(backend)


@app.get("/auth/complete/{backend}/", name="auth_complete_get")
@app.post("/auth/complete/{backend}/", name="auth_complete_post")
@psa("complete")
async def auth_complete(backend: str, request: Request):
    return do_complete(backend, login=do_login, request=request, *args, **kwargs)


@app.get("/auth/saml_metadata/{backend}/", name="auth_saml_metadata_get")
def saml_metadata_view(backend: str, request: Request):
    complete_url = app.url_path_for("auth_complete_get", backend=backend)

    strategy = load_strategy(request)

    saml_backend = load_backend(strategy, "social_core.backends.saml.SAMLAuth", complete_url)

    metadata, errors = saml_backend.generate_metadata_xml()

    if not errors:
        return Response(content=metadata, media_type="application/xml")

    return Response(content=", ".join(errors))


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("social_app_fastapi_sqlalchemy.main:app", host="0.0.0.0", port=8000, reload=True)
