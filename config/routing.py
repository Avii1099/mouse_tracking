from django.urls import path

from tracking.core.mouse_tracker.consumers import ImagesConsumer

websocket_urls = [
    path("fetch-image/", ImagesConsumer.as_asgi()),
]
