import uvicorn
from fastapi import FastAPI, Response
from social_core.actions import do_auth, do_complete
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from .decorators import psa
from .utils import do_login, load_backend, load_strategy

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="some-random-string")


@app.get("/", name="root_get")
@app.post("/", name="root_post")
async def root(request: Request):
    return {"message": "Hello World"}


@app.get("/auth/login/{backend}/", name="auth_login")
@app.post("/auth/login/{backend}/", name="auth_login")
@psa("auth_complete")
def auth_login(request: Request, backend: str):
    return do_auth(backend)


@app.get("/auth/complete/{backend}/", name="auth_complete")
@app.post("/auth/complete/{backend}/", name="auth_complete")
@psa("auth_complete")
def auth_complete(request: Request, backend: str):
    return do_complete(backend, login=do_login, request=request)


@app.get("/auth/saml_metadata/{backend}/", name="auth_saml_metadata_get")
def saml_metadata_view(backend: str, request: Request):
    complete_url = app.url_path_for("auth_complete", backend=backend)

    strategy = load_strategy(request)

    saml_backend = load_backend(strategy, "social_core.backends.saml.SAMLAuth", complete_url)

    metadata, errors = saml_backend.generate_metadata_xml()

    if not errors:
        return Response(content=metadata, media_type="application/xml")

    return Response(content=", ".join(errors))


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("social_app_fastapi_sqlalchemy.main:app", host="0.0.0.0", port=8000, reload=True)
