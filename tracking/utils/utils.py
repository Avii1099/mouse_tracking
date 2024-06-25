from tracking.services.websocket_wrapper import WebSocketWrapper


def send_images(instance):
    try:
        WebSocketWrapper().send_images_socket(instance)
    except Exception as e:
        print("send_images", e)
