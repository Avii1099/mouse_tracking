from django.urls import path, include
from .views import TrackingView, TrackDetailsTemplateView, MouseEventView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("mouse-events", MouseEventView, basename="mouse-events")

urlpatterns = [
    path("", TrackDetailsTemplateView.as_view(), name="track"),
    path("api/", include(router.urls), name="chat-app"),
    path("start_track/", TrackingView.as_view(), name="start_track"),
]
