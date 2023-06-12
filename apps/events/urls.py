from django.urls import path 
from .views import events

urlpatterns = [
    path("events/", events, name="events")
]