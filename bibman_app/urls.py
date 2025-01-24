from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView,
    MajorCreateView,MajorListView,MajorDeleteView,MajorUpdateView
)

urlpatterns = [
     # Students
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/add/", StudentCreateView.as_view(), name="student-create"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student-edit"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

    # Professors
    path("professors/", ProfessorListView.as_view(), name="professor-list"),
    path("professors/add/", ProfessorCreateView.as_view(), name="professor-create"),
    path("professors/<int:pk>/edit/", ProfessorUpdateView.as_view(), name="professor-edit"),
    path("professors/<int:pk>/delete/", ProfessorDeleteView.as_view(), name="professor-delete"),

    # Majors (Especialidades)
    path('majors/', MajorListView.as_view(), name='major-list'),
    path('majors/add/', MajorCreateView.as_view(), name='major-create'),
    path('majors/<int:pk>/edit/', MajorUpdateView.as_view(), name='major-edit'),
    path('majors/<int:pk>/delete/', MajorDeleteView.as_view(), name='major-delete'),

]
