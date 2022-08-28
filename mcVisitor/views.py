from django.shortcuts import render
from django.views import generic


class vHomeview(generic.TemplateView):
    login_required = True
    template_name = "mcVisitor/vhome.html"
    extra_context = {"page_title": "Home"}
