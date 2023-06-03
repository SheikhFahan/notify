from django.urls import path, include
from django.conf import urls
from . import views

urlpatterns = [
    path("", views.api_home)
]
