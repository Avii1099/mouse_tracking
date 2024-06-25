import asyncio

from channels.layers import get_channel_layer

from tracking.core.mouse_tracker.models import MouseEvent
from tracking.core.mouse_tracker.serializers import MouseEventSerializers


class WebSocketWrapper:
    async def broadcast_websocket_message_async(
        self, group_name: str, payload: dict
    ) -> None:
        """_summary_

        Args:
            group_name (str): Channel Group Name
            payload (dict): Message to be Send
        """

        try:
            channel_layer = get_channel_layer()

            await channel_layer.group_send(
                group_name, {"type": "broadcast_message", "message": payload}
            )
        except Exception as e:
            print("broadcast_websocket_message_async: ", e)

    def broadcast_websocket_message(self, group_name: str, payload: dict) -> None:
        """_summary_

        Args:
            group_name (str): Channel Group Name
            payload (dict): Message to be Send
        """

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                self.broadcast_websocket_message_async(group_name, payload)
            )
            print("Done")
            loop.close()
        except Exception as e:
            print("broadcast_websocket_message: ", e)

    def send_images_socket(self, instance: MouseEvent) -> None:
        """_summary_

        Args:
            instance (Notification):
        """
        # queryset = MouseEvent.objects.order_by("-created_at")[:10]
        payload = MouseEventSerializers(instance).data
        self.broadcast_websocket_message("mouse_track", payload)
