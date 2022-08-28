from django.shortcuts import render
from django.views import generic


class sHomeview(generic.TemplateView):
    login_required = True
    template_name = "mcStudent/shome.html"
    extra_context = {"page_title": "Home"}
