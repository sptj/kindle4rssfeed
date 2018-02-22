import web
import os, sys

urls = (
    '/(.*)', 'hello'
)


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', int(port)))
    app.run()
# import os
# import web
# from weixinInterface import WeixinInterface
#
# urls = (
# '/weixin','WeixinInterface'
# )
#
# app_root = os.path.dirname(__file__)
# templates_root = os.path.join(app_root, 'templates')
# render = web.template.render(templates_root)
# if __name__ == "__main__":
#     port = os.environ.get("PORT", "5000")
#     app = web.application(urls, globals())
#     web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', int(port)))
#     app.run()
