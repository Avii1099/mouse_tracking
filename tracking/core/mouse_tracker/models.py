from django.db import models
from tracking.base.models import BaseModel


class MouseEvent(BaseModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    image_path = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"Mouse event at ({self.x_coordinate}, {self.y_coordinate}) recorded at {self.timestamp}"
