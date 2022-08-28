from json import dumps
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from mainCore.models import Teacher, Classe, Eleve, Presence
from .forms import addStudentForm, addClasseForm, addTeacherForm
from users.models import Profile

User = get_user_model()


class o_listTeacher(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_listTeacher.html"

    def get(self, request, *args, **kwargs):
        listTeacher = Teacher.objects.all()
        context = {"listTeacher": listTeacher, "page_title": "List Teacher"}
        return render(request, self.template_name, context)


class dtteacher(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        data = list(Teacher.objects.values())
        return JsonResponse(data, safe=False)


class o_listClasses(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_listclass.html"
    extra_context = {"page_title": "Class List"}

    def get(self, request, *args, **kwargs):
        listClass = Classe.objects.all().order_by("Classe_name")
        context = {"listClass": listClass}
        return render(request, self.template_name, context)


class dtclasses(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        data = list(Classe.objects.values())
        return JsonResponse(data, safe=False)


class o_listStudent(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_listStud.html"
    page_title = "Student List"

    def get_context_data(self, **kwargs):
        context = super(o_listStudent, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["klasname"] = self.kwargs["klasname"]
        context["skooY"] = self.kwargs["skooY"]
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["page_title"] = self.page_title
        context["testDT"] = serializers.serialize(
            "json", Eleve.objects.filter(class_id=pk)
        )
        return context


class dashClass(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/dashboard_class.html"
    page_title = "Dashboard Classe"

    def get_context_data(self, **kwargs):
        context = super(dashClass, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["classes"] = Classe.objects.filter(pk=pk)
        context["numblistStuds"] = Eleve.objects.filter(class_id=pk).count()
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["page_title"] = self.page_title
        return context


class o_view_student(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_student_details.html"

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        if pk == None:
            student = {}
        elif pk > 0:
            student = Eleve.objects.filter(id=pk).first()
        else:
            student = {}
        return render(request, self.template_name, {"student": student})


class AddTeacher(LoginRequiredMixin, generic.TemplateView):
    form_class = addTeacherForm
    template_name = "mcOverseer/addTeacher.html"
    page_title = "Add Teacher"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": self.page_title}
        return render(request, self.template_name, context)

    def addT(self, username, email, dob, name, name1, pob, gender):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=dob,
            is_visitor=False,
            is_teacher=True,
        )
        Teacher.objects.create(
            user=user,
            nom=name,
            prenom=name1,
            dob=dob,
            pob=pob,
            gender=gender,
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        name = request.POST.get("nom")
        name1 = request.POST.get("prenom")
        username = f"{name}_{name1}"
        dob = request.POST.get("dob")
        pob = request.POST.get("pob")
        gender = request.POST.get("gender")
        email = "{}@example.com".format(username)
        if form.is_valid:
            self.addT(username, email, dob, name, name1, pob, gender)
            return redirect("mcOverseer:o_listTeacher")


class AddClasses(LoginRequiredMixin, generic.TemplateView):
    form_class = addClasseForm
    template_name = "mcOverseer/addClasses.html"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": "Add Classe"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            form.save()
            return redirect("mcOverseer:o_listClasses")


class AddStudentes(LoginRequiredMixin, generic.TemplateView):
    form_class = addStudentForm
    template_name = "mcOverseer/addStud.html"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": "Add Studente"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        name = request.POST.get("nom")
        name1 = request.POST.get("prenom")
        username = f"{name}_{name1}"
        dob = request.POST.get("dob")
        pob = request.POST.get("pob")
        gender = request.POST.get("gender")
        classe = request.POST.get("class_id")
        email = "{}@example.com".format(username)
        if form.is_valid:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=dob,
                is_visitor=False,
                is_student=True,
            )
            Eleve.objects.create(
                user=user,
                nom=name,
                prenom=name1,
                dob=dob,
                pob=pob,
                gender=gender,
                class_id=Classe.objects.filter(pk=classe).first(),
            )
            return redirect("mcOverseer:o_listClasses")


class o_Att(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_att.html"

    def get(self, request, *args, **kwargs):
        klasname = self.kwargs["klasname"]
        listPresence = Presence.objects.all().order_by("attendance_date")
        context = {
            "listPresence": listPresence,
            "klasname": klasname,
            "page_title": "Test",
        }
        return render(request, self.template_name, context)


class o_Att_by_date(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_att.html"
    page_title = "Test o_Att_by_date"

    def get_context_data(self, **kwargs):
        context = super(o_Att_by_date, self).get_context_data(**kwargs)
        att_date = self.kwargs["att_date"]
        context["listPresence"] = Presence.objects.filter(attendance_date=att_date)
        context["klasname"] = self.kwargs["klasname"]
        context["page_title"] = self.page_title
        return context


class o_AttMgt(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/o_attmgt.html"
    page_title = "Student List"

    def get_context_data(self, **kwargs):
        context = super(o_AttMgt, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["klasname"] = self.kwargs["klasname"]
        context["skooY"] = self.kwargs["skooY"]
        context["class_id"] = pk
        context["page_title"] = self.page_title
        return context


class confirm(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, *args, **kwargs):
        class_id = self.kwargs["class_id"]
        listStuds = Eleve.objects.filter(class_id=class_id)
        for student in listStuds:
            status = request.POST[student.student_code]
            if status != "present":
                status = "False"
            status = "True"
            date_ = request.POST["mydate"]
            a = Presence(student=student, attendance_date=date_, status=status)
            a.save()
        return HttpResponse("Ok")


def confirms(request, class_id=None):
    listStuds = Eleve.objects.filter(class_id=class_id)
    if request.method == "POST":
        for student in listStuds:
            status = request.POST[student.student_code]
            if status == "present":
                status = "True"
            else:
                status = "False"
            date_ = request.POST.get("mydate")
            a = Presence(student=student, attendance_date=date_, status=status)
            a.save()
        return HttpResponse("Ok")


class oHomeview(LoginRequiredMixin, generic.TemplateView):
    template_name = "mcOverseer/ohome.html"
    extra_context = {"page_title": "Home"}
