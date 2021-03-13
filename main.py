from aiohttp import web
import aiohttp_jinja2
import jinja2
# настроим url-пути для доступа к нашему будущему приложению
def setup_routes(application):
    from app.forum.routes import setup_routes as setup_forum_routes

    setup_forum_routes(application)
def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application,
         loader=jinja2.FileSystemLoader("templates")
    )
def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)
    print('app setup succeed')

app = web.Application() # создаем наш веб-сервер
# эта строка пригодится нам в будущем
if __name__ == "__main__":
    setup_app(app)
    web.run_app(app) # запускаем наше приложение