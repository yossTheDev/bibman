from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView,
    MajorCreateView,MajorListView,MajorDeleteView,MajorUpdateView,
    DepartmentCreateView,DepartmentListView,DepartmentDeleteView,DepartmentUpdateView,
    FacultyCreateView,FacultyListView,FacultyDeleteView,FacultyUpdateView,
    AccessRecordListView,AccessRecordCreateView,AccessRecordDeleteView,AccessRecordUpdateView
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

    # Department URLs
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/add/', DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department-edit'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),

     # Faculty URLs
    path('faculties/', FacultyListView.as_view(), name='faculty-list'),
    path('faculties/add/', FacultyCreateView.as_view(), name='faculty-create'),
    path('faculties/<int:pk>/edit/', FacultyUpdateView.as_view(), name='faculty-edit'),
    path('faculties/<int:pk>/delete/', FacultyDeleteView.as_view(), name='faculty-delete'),

     # AccessRecord URLs
    path('access_records/', AccessRecordListView.as_view(), name='access-record-list'),
    path('access_records/add/', AccessRecordCreateView.as_view(), name='access-record-create'),
    path('access_records/<int:pk>/edit/', AccessRecordUpdateView.as_view(), name='access-record-edit'),
    path('access_records/<int:pk>/delete/', AccessRecordDeleteView.as_view(), name='access-record-delete'),

]
