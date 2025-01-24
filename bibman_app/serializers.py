from rest_framework import serializers
from .models import Student, Professor

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

# Professor Serializer
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__' 
