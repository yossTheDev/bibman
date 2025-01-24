from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Person, Student, Professor,Major, Department
from .forms import  StudentForm, ProfessorForm, MajorForm
from .serializers import StudentSerializer, ProfessorSerializer

def home(request):
    return render(request, 'home.html') 

# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Professor ViewSet
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


# Views for Student Model
    
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student-list")


# Views for Professor Model
class ProfessorListView(ListView):
    model = Professor
    template_name = "professors/professor_list.html"
    context_object_name = "professors"


class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "professors/professor_form.html"
    success_url = reverse_lazy("professor-list")


class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "professors/professor_form.html"
    success_url = reverse_lazy("professor-list")


class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = "professors/professor_confirm_delete.html"
    success_url = reverse_lazy("professor-list")

    model = Professor
    template_name = "professors/professor_confirm_delete.html"
    success_url = reverse_lazy("professor-list")


    # List all Majors
class MajorListView(ListView):
    model = Major
    template_name = 'major/major_list.html'
    context_object_name = 'majors'

# Create a new Major
class MajorCreateView(CreateView):
    model = Major
    template_name = 'major/major_form.html'
    form_class = MajorForm
    success_url = reverse_lazy('major-list')

# Edit an existing Major
class MajorUpdateView(UpdateView):
    model = Major
    template_name = 'major/major_form.html'
    form_class = MajorForm
    success_url = reverse_lazy('major-list')

# Delete a Major
class MajorDeleteView(DeleteView):
    model = Major
    template_name = 'major/major_confirm_delete.html'
    success_url = reverse_lazy('major-list')


# List View for Department
class DepartmentListView(ListView):
    model = Department
    template_name = "departments/department_list.html"
    context_object_name = "departments"

# Create View for Department
class DepartmentCreateView(CreateView):
    model = Department
    template_name = "departments/department_form.html"
    fields = ['name', 'faculty']  # Fields you want to show in the form
    success_url = reverse_lazy("department-list")

# Update View for Department
class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = "departments/department_form.html"
    fields = ['name', 'faculty']
    success_url = reverse_lazy("department-list")

# Delete View for Department
class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "departments/department_confirm_delete.html"
    success_url = reverse_lazy("department-list")