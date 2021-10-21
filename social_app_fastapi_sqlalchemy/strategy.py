import asyncio
import json
import os

from social_core.strategy import BaseStrategy, BaseTemplateStrategy
from social_core.utils import build_absolute_uri
from starlette.templating import Jinja2Templates

from . import settings


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

        # Force text on URL named settings that are instance of Promise
        if name.endswith("_URL"):
            if isinstance(value, Promise):
                value = force_str(value)
            value = resolve_url(value)
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
        if self.request:
            return f"{self.request.url.scheme}://{self.request.url.hostname}:{self.request.url.port}"

    def redirect(self, url):
        return redirect(url)

    def html(self, content):
        response = make_response(content)
        response.headers["Content-Type"] = "text/html;charset=UTF-8"
        return response

    def session_get(self, name, default=None):
        return session.get(name, default)

    def session_set(self, name, value):
        session[name] = value

    def session_pop(self, name):
        return session.pop(name, None)

    def session_setdefault(self, name, value):
        return session.setdefault(name, value)

    def build_absolute_uri(self, path=None):
        return build_absolute_uri(self.request_host(), path)
