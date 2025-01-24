from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Person, Student, Professor
from .forms import  StudentForm, ProfessorForm
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