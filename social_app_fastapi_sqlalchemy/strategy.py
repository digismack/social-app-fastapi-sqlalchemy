from collections import namedtuple
import asyncio
import json
import os

from social_core.strategy import BaseStrategy, BaseTemplateStrategy
from social_core.utils import build_absolute_uri
from starlette.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

SETTINGS_FILE = "settings.json"

with open(SETTINGS_FILE) as f:
    data = json.load(f)
    settings = namedtuple('settings', data.keys())(*data.values())


class FastAPITemplateStrategy(BaseTemplateStrategy):
    def render_template(self, tpl, context):
        return render_template(tpl, **context)

    def render_string(self, html, context):
        return render_template_string(html, **context)


class FastAPIStrategy(BaseStrategy):
    DEFAULT_TEMPLATE_STRATEGY = FastAPITemplateStrategy

    def __init__(self, storage, request=None, tpl=None):
        self.request = request
        self.session = request.session if request else {}
        super().__init__(storage, tpl)

    def get_setting(self, name):
        if isinstance(settings, dict):
            value = settings.get(name)
        else:
            value = getattr(settings, name)
        return value

    def request_data(self, merge=True):
        if not self.request:
            return {}

        if merge:
            data = dict(self.request.query_params)
            data.update(dict(asyncio.run(self.request.form())))
        elif self.request.method == "POST":
            data = dict(asyncio.run(self.request.form()))
        else:
            data = dict(self.request.query_params)
        return data

    def request_host(self):
        return f"{self.request.url.hostname}:{self.request.url.port}"

    def request_is_secure(self):
        return self.request.url.scheme == "https"

    def request_path(self):
        return self.request.url.path

    def request_port(self):
        return self.request.url.port

    def request_get(self):
        return dict(self.request.query_params)

    def request_post(self):
        return dict(asyncio.run(self.request.form()))

    def redirect(self, url):
        return RedirectResponse(url)

    def html(self, content):
        response = make_response(content)
        response.headers["Content-Type"] = "text/html;charset=UTF-8"
        return response

    def session_get(self, name, default=None):
        return self.session.get(name, default)

    def session_set(self, name, value):
        self.session[name] = value

    def session_pop(self, name):
        return self.session.pop(name, None)

    def session_setdefault(self, name, value):
        return self.session.setdefault(name, value)

    def build_absolute_uri(self, path=None):
        if self.request:
            return build_absolute_uri(f"{self.request.url.scheme}://{self.request_host()}", path)
        else:
            return path
