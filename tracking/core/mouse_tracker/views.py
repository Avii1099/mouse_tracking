from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from django.views.generic import TemplateView
from django.core.management import call_command
import threading
from django.http import HttpResponse
from .serializers import MouseEventSerializers
from .models import MouseEvent


# Create your views here.
monitor_thread = None


class TrackingView(View):

    def get(self, request):
        global monitor_thread

        if monitor_thread is None or not monitor_thread.is_alive():
            monitor_thread = threading.Thread(
                target=call_command, args=("start_mouse_monitor",)
            )
            monitor_thread.daemon = True
            monitor_thread.start()
            return HttpResponse("Tracking started", status=200)
        else:
            return HttpResponse("Already tracking", status=200)


class TrackDetailsTemplateView(TemplateView):
    template_name = "mouse_tracker/tracker.html"


class MouseEventView(ModelViewSet):
    queryset = MouseEvent.objects.order_by("-created_at")[:10]
    serializer_class = MouseEventSerializers
