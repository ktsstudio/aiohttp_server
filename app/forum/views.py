import aiohttp_jinja2
from aiohttp import web
# создаем функцию, которая будет отдавать html-файл
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {'title': 'Пишем первое приложение на aiohttp'}