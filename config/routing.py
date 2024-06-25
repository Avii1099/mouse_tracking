from django.urls import path

from tracking.core.mouse_tracker.consumers import ImagesConsumer, MouseCoordinates

websocket_urls = [
    path("fetch-image/", ImagesConsumer.as_asgi()),
    path("mouse-coordinates/", MouseCoordinates.as_asgi()),
]
