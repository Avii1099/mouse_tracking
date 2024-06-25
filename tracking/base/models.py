from django.conf import settings
from django.db import models
from django.forms.models import model_to_dict


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict(self):
        data = model_to_dict(self)
        data["created_at"] = self.created_at
        data["updated_at"] = self.updated_at
        return data

    def get_image_url(self, image_url):
        return settings.MEDIA_URL + image_url
