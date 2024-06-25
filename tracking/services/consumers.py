import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class BaseWebsocketConsumer(AsyncWebsocketConsumer):

    channel_layer = get_channel_layer()
    group_name = ""

    async def connect(self, **kwargs):
        self.room_name = "mouse_track"
        self.room_group_name = self.room_name
        print("self.room_group_name: ", self.room_group_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code, **kwargs):

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, **kwargs):

        try:
            data = json.loads(text_data)
        except Exception:
            data = text_data

        if data == "ping":
            data = "pong"

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "broadcast_message", "message": data}
        )

    async def broadcast_message(self, event):
        message = event["message"]
        print("broadcast_message: message: ", message)
        try:
            await self.send(text_data=json.dumps(message))
        except Exception:
            await self.close()
