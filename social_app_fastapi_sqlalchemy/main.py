import uvicorn
from fastapi import FastAPI, Response
from social_core.actions import do_auth, do_complete
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware

from .decorators import psa
from .utils import do_login, load_backend, load_strategy


app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="some-random-string")


@app.get("/")
@app.post("/")
async def root(request: Request):
    print(dict(request.query_params))
    print(dict(await request.form()))
    base_url = f"{request.url.scheme}://{request.url.hostname}:{request.url.port}"
    print(base_url)

    return {"message": "Hello World"}


@app.get("/auth/login/{backend}/")
@app.post("/auth/login/{backend}/")
@psa("complete")
async def auth_login(backend: str, request: Request):
    return do_auth(backend)


@app.get("/auth/complete/{backend}/")
@app.post("/auth/complete/{backend}/")
@psa("complete")
async def auth_complete(backend: str, request: Request):
    return do_complete(backend, login=do_login, request=request, *args, **kwargs)


@app.get("/auth/saml_metadata/{backend}/")
def saml_metadata_view(backend: str, request: Request):
    # complete_url = reverse('complete', args=(backend, ))

    strategy = load_strategy(request)

    saml_backend = load_backend(strategy, "social_core.backends.saml.SAMLAuth", redirect_uri="")  # complete_url)

    metadata, errors = saml_backend.generate_metadata_xml()

    if not errors:
        return Response(content=metadata, media_type="application/xml")

    return Response(content=", ".join(errors))


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("social_app_fastapi_sqlalchemy.main:app", host="0.0.0.0", port=8000, reload=True)
