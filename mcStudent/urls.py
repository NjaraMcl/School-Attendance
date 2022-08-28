from django.urls import path
from . import views

app_name = "mcStudent"

urlpatterns = [
    path("shome/", views.sHomeview.as_view(), name="shome"),
]
