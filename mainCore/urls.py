from django.urls import path
from . import views

app_name = "mainCore"

urlpatterns = [
    path("", views.Homeview.as_view(), name="home"),
    path("ghome/", views.gHomeview.as_view(), name="ghome"),
]
