from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/v1/devices/", IndexAPIView.as_view(), name="devices"),
    path("api/v1/devices1/", DeviceAPIView.as_view(), name="devices"),
    path("api/v1/selectcard/", SelectedCardAPIView.as_view(), name="card"),
    path("api/v1/add-description/", AddDescriptionAPIView.as_view())
]

