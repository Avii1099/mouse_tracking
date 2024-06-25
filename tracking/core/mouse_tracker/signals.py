from django.db.models.signals import post_save
from django.dispatch import receiver

from tracking.utils.utils import send_images

from .models import MouseEvent


@receiver(post_save, sender=MouseEvent)
def trigger_notification(sender, instance, created, **kwargs):
    send_images(instance)
