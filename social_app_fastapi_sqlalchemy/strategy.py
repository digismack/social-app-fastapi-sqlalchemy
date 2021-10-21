from social_core.strategy import BaseStrategy, BaseTemplateStrategy
from social_core.utils import build_absolute_uri
from starlette.templating import Jinja2Templates


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
        return current_app.config[name]

    async def request_data(self, merge=True):
        if not self.request:
            return {}

        if merge:
            data = dict(self.request.params)
            data.update(dict(await request.form()))
        elif self.request.method == "POST":
            data = dict(await request.form())
        else:
            data = dict(request.query_params)
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
