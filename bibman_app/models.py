from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Faculty name

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)  # Department name
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="departments")

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"


class Major(models.Model):
    name = models.CharField(max_length=255)  # Major or specialization name
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="majors")

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"


class Person(models.Model):
    name = models.CharField(max_length=255)  # Full name
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="persons")  # Faculty
    created_at = models.DateTimeField(auto_now_add=True)  # To track creation time

    def __str__(self):
        return f"{self.name}"


class Student(Person):
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
    academic_year = models.PositiveSmallIntegerField()  # Academic year (1-5)

    def __str__(self):
        return f"Student: {self.name}, Year {self.academic_year}"


class Professor(Person):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name="professors")

    def __str__(self):
        return f"Professor: {self.name}, {self.department.name if self.department else 'No Department'}"


class AccessRecord(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="access_records")  # Person who accessed
    timestamp = models.DateTimeField(auto_now_add=True)  # Access timestamp
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)  # For students, if applicable
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)  # For professors, if applicable

    def __str__(self):
        return f"Access: {self.person.name} at {self.timestamp}"

