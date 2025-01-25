from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Person, Student, Professor,Major, Department, Faculty, AccessRecord
from .forms import  StudentForm, ProfessorForm, MajorForm,AccessRecordForm
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

    def get_queryset(self):
        queryset = super().get_queryset()

        # Getting filters from GET request
        name = self.request.GET.get('name')
        major = self.request.GET.get('major')
        academic_year = self.request.GET.get('academic_year')

        # Filtering based on the query parameters
        if name:
            queryset = queryset.filter(name__icontains=name)
        if major:
            queryset = queryset.filter(major_id=major)
        if academic_year:
            queryset = queryset.filter(academic_year=academic_year)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['majors'] = Major.objects.all()  # Make sure 'Major' is your correct model
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['majors'] = Major.objects.all()  # Ensure that you're passing all majors to the context
        context['departments'] = Department.objects.all()  # Ensure that you're passing all departments to the context

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get filter values from the GET request
        name = self.request.GET.get('name')
        major = self.request.GET.get('major')
        academic_year = self.request.GET.get('academic_year')

        # Filter professors based on the request parameters
        if name:
            queryset = queryset.filter(name__icontains=name)
        if major:
            queryset = queryset.filter(major_id=major)
        if academic_year:
            queryset = queryset.filter(academic_year=academic_year)

        return queryset

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
    template_name = "major/major_list.html"
    context_object_name = "majors"

    def get_queryset(self):
        # Start with the base queryset
        queryset = super().get_queryset()

        # Get filter values from GET request
        name = self.request.GET.get('name')
        faculty = self.request.GET.get('faculty')

        # If name filter is provided, filter majors by name
        if name:
            queryset = queryset.filter(name__icontains=name)

        # If faculty filter is provided, filter majors by faculty
        if faculty:
            queryset = queryset.filter(faculty__id=faculty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add list of faculties to the context for filtering
        context['faculties'] = Faculty.objects.all()
        return context
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

    def get_queryset(self):
        # Start with the base queryset
        queryset = super().get_queryset()

        # Get filter values from GET request
        name = self.request.GET.get('name')
        faculty = self.request.GET.get('faculty')

        # If name filter is provided, filter departments by name
        if name:
            queryset = queryset.filter(name__icontains=name)

        # If faculty filter is provided, filter departments by faculty
        if faculty:
            queryset = queryset.filter(faculty__id=faculty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add list of faculties to the context for filtering
        context['faculties'] = Faculty.objects.all()
        return context

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


# List View for Faculty
class FacultyListView(ListView):
    model = Faculty
    template_name = "faculties/faculty_list.html"
    context_object_name = "faculties"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get filter values from the GET request
        name = self.request.GET.get('name')

        # Filter faculties based on the request parameters
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


# Create View for Faculty
class FacultyCreateView(CreateView):
    model = Faculty
    template_name = "faculties/faculty_form.html"
    fields = ['name']  # Fields you want to show in the form
    success_url = reverse_lazy("faculty-list")

# Update View for Faculty
class FacultyUpdateView(UpdateView):
    model = Faculty
    template_name = "faculties/faculty_form.html"
    fields = ['name']
    success_url = reverse_lazy("faculty-list")

# Delete View for Faculty
class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = "faculties/faculty_confirm_delete.html"
    success_url = reverse_lazy("faculty-list")


class AccessRecordListView(ListView):
    model = AccessRecord
    template_name = "access_records/access_record_list.html"
    context_object_name = "access_records"

class AccessRecordCreateView(CreateView):
    model = AccessRecord
    form_class = AccessRecordForm
    template_name = "access_records/access_record_form.html"
    success_url = reverse_lazy('access-record-list')

class AccessRecordUpdateView(UpdateView):
    model = AccessRecord
    form_class = AccessRecordForm
    template_name = "access_records/access_record_form.html"
    success_url = reverse_lazy('access-record-list')

class AccessRecordDeleteView(DeleteView):
    model = AccessRecord
    template_name = "access_records/access_record_confirm_delete.html"
    success_url = reverse_lazy('access-record-list')