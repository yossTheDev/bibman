from django import forms
from .models import Person, Student, Professor


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "role", "faculty"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "faculty": forms.Select(attrs={"class": "form-control"}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["person", "major", "academic_year"]
        widgets = {
            "person": forms.Select(attrs={"class": "form-control"}), 
            "major": forms.Select(attrs={"class": "form-control"}),   
            "academic_year": forms.NumberInput(attrs={"class": "form-control"}),  
        }


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["person", "department"]
        widgets = {
            "person": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
        }
