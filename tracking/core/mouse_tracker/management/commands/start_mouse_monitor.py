import cv2
import numpy as np
import time
from django.core.management.base import BaseCommand
from evdev import InputDevice, categorize, ecodes, list_devices
from tracking.core.mouse_tracker.models import MouseEvent
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from tracking.services.websocket_wrapper import WebSocketWrapper


class Command(BaseCommand):
    help = "Starts the background thread to monitor mouse events"

    def find_mouse_device(self):
        for path in list_devices():
            device = InputDevice(path)
            if ecodes.EV_REL in device.capabilities() and (
                ecodes.REL_X in device.capabilities()[ecodes.EV_REL]
                and ecodes.REL_Y in device.capabilities()[ecodes.EV_REL]
            ):
                return device.path
        return None

    def handle(self, *args, **options):

        should_continue_tracking = True

        find_mouse_device = self.find_mouse_device()
        device = InputDevice(
            find_mouse_device if find_mouse_device else "/dev/input/event18"
        )

        x_total = 0
        y_total = 0

        print("Starting to track mouse movements...")
        try:
            for event in device.read_loop():
                if not should_continue_tracking:
                    print("Stopping the mouse tracker.")
                    break
                if event.type == ecodes.EV_REL:
                    if event.code == ecodes.REL_X:
                        x_total += event.value
                    elif event.code == ecodes.REL_Y:
                        y_total += event.value
                    WebSocketWrapper().send_coordinates_socket(
                        [{"x_total": x_total, "y_total": y_total}]
                    )
                elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_LEFT:
                    if event.value == 1:  # Button pressed
                        print(f"Left button clicked at X:{x_total}, Y:{y_total}")
                        should_continue_tracking = False
                        self.capture_image(x_total, y_total)
        except KeyboardInterrupt:
            print("Stopping the mouse tracker.")

    def capture_image(self, x_coordinate, y_coordinate):
        cam = cv2.VideoCapture(0)  # Default camera
        ret, frame = cam.read()
        if ret:
            # Convert the image to a format that Django can save
            _, buffer = cv2.imencode(".jpg", frame)
            content_file = ContentFile(buffer.tobytes())

            # Create a new instance of the model where the image will be stored
            mouse_event = MouseEvent(
                x_coordinate=x_coordinate,
                y_coordinate=y_coordinate,
                image_path=content_file,
            )
            file_name = time.strftime("%Y-%m-%d_%H-%M-%S")

            mouse_event.image_path.save(f"{file_name}.jpg", content_file, save=True)

            cam.release()
            return mouse_event.image_path.url  # Returns the URL to access the image
        cam.release()
        return None
