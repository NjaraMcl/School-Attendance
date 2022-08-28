from django.shortcuts import redirect
from django.views import generic


class gHomeview(generic.TemplateView):
    template_name = "mainCore/ghome.html"
    extra_context = {"page_title": "Home"}


class Homeview(generic.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("mainCore:ghome")
        if request.user.is_visitor:
            return redirect("mcVisitor:vhome")
        if request.user.is_student:
            return redirect("mcStudent:shome")
        if request.user.is_teacher:
            return redirect("mcTeacher:thome")
        if request.user.is_overseer:
            return redirect("mcOverseer:ohome")
