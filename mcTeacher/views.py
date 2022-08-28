from django.shortcuts import render
from django.views import generic


class tHomeview(generic.TemplateView):
    login_required = True
    template_name = "mcTeacher/thome.html"
    extra_context = {"page_title": "Home"}
