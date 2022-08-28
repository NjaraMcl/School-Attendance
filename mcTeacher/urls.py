from django.urls import path
from . import views

app_name = "mcTeacher"

urlpatterns = [
    path("thome/", views.tHomeview.as_view(), name="thome"),
]
