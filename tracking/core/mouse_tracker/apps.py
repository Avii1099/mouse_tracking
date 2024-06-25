from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MouseTrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracking.core.mouse_tracker"
    verbose_name = _("Mouse Tracker")

    def ready(self) -> None:
        import tracking.core.mouse_tracker.signals
