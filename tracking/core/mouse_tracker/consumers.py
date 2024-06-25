from tracking.services.consumers import BaseWebsocketConsumer


class ImagesConsumer(BaseWebsocketConsumer):
    """
    Purchase Research Consumer
    """

    async def connect(self, **kwargs):
        await super().connect()

    async def disconnect(self, close_code, **kwargs):
        await super().disconnect(close_code)

    async def receive(self, **kwargs):
        await super().receive(self, **kwargs)


class MouseCoordinates(BaseWebsocketConsumer):
    async def connect(self, **kwargs):
        await super().connect(prefix="mouseCoordinates")

    async def disconnect(self, close_code, **kwargs):
        await super().disconnect(close_code, prefix="mouseCoordinates")

    async def receive(self, **kwargs):
        await super().receive(self, **kwargs, prefix="mouseCoordinates")
