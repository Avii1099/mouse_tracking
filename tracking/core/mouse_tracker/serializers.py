from rest_framework import serializers
from .models import MouseEvent


class MouseEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = MouseEvent
        fields = [
            "timestamp",
            "x_coordinate",
            "y_coordinate",
            "image_path",
        ]
