from django.urls import path

from . import views

app_name = "ntrfc"
urlpatterns = [
  path("", views.index, name="index"),
  path("city/", views.city, name="city"),
]
