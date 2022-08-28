from django.urls import path
from . import views

app_name = "mcOverseer"

urlpatterns = [
    path("ohome/", views.oHomeview.as_view(), name="ohome"),
    path("ohome/listTeacher/", views.o_listTeacher.as_view(), name="o_listTeacher"),
    path("ohome/dtTeacher/", views.dtteacher.as_view(), name="dtTeacher"),
    path("ohome/listClasses/", views.o_listClasses.as_view(), name="o_listClasses"),
    path("ohome/dtClasses/", views.dtclasses.as_view(), name="dtClasses"),
    path("ohome/listClasses/<int:pk>", views.dashClass.as_view(), name="dashClass"),
    path(
        "ohome/listStudent/<int:pk>/<str:klasname>/<str:skooY>",
        views.o_listStudent.as_view(),
        name="o_listStudent",
    ),
    path(
        "o_viewstudent/<int:pk>",
        views.o_view_student.as_view(),
        name="o_studentdetail-modal",
    ),
    path("ohome/addteacher/", views.AddTeacher.as_view(), name="AddTeacher"),
    path("ohome/addclasse/", views.AddClasses.as_view(), name="AddClasses"),
    path("ohome/addstudent/", views.AddStudentes.as_view(), name="AddStudentes"),
    path(
        "ohome/listClasses/<str:klasname>/o_attendence/",
        views.o_Att.as_view(),
        name="o_attendence",
    ),
    path(
        "ohome/listClasses/<str:klasname>/<str:skooY>/<int:pk>/o_attmgt/",
        views.o_AttMgt.as_view(),
        name="o_attmgt",
    ),
    path(
        "ohome/listClasses/<int:class_id>/confirm",
        views.confirm.as_view(),
        name="confirm",
    ),
]
