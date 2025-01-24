from django import forms
from .models import Student, Professor, Major, Department, Faculty

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "faculty", "major", "academic_year"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "faculty": forms.Select(attrs={"class": "form-control"}),
            "major": forms.Select(attrs={"class": "form-control"}),
            "academic_year": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["name", "faculty", "department"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "faculty": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
        }

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['name', 'faculty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }