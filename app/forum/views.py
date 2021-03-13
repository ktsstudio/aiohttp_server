import aiohttp_jinja2
from aiohttp import web
from app.forum.models import Message
from datetime import datetime


@aiohttp_jinja2.template("index.html")
async def index(_):
    return {'title': 'Пишем первое приложение на aiohttp'}


class ListMessageView(web.View):
    async def get(self):
        messages = await Message.query.order_by(Message.id.desc()).gino.all()
        messages_data = []
        for message in messages:
            messages_data.append(
                {
                    "id": message.id,
                    "text": message.text,
                    "created": str(message.created),
                }
            )
        return web.json_response(data={'messages': messages_data})


class CreateMessageView(web.View):
    async def post(self):
        data = await self.request.json()
        message = await self.request.app["db"].message.create(
            text=data['text'],
            created=datetime.now(),
        )
        return web.json_response(data={'message': {
            'id': message.id,
            'text': message.text,
            'created': str(message.created),
        }})
