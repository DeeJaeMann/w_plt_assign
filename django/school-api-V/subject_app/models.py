from django.db import models
from django.core import validators as v

from .validators import validate_subject_format, validate_professor_name

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=100, default="Professor Cahan", validators=[validate_professor_name])
    # students = created by related_name relationship in Students.subjects

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}"

    def add_a_student(self, int_student_id):
        from grade_app.models import Student
        int_students_length = self.students.count()

        if int_students_length < 31:
            student = Student.objects.get(id=int_student_id)
            self.students.add(student)
        else:
            raise Exception("This subject is full!")
        
    def drop_a_student(self, int_student_id):
        from grade_app.models import Student

        int_students_length = self.students.count()

        if int_students_length > 0:
            student = Student.objects.get(id=int_student_id)
            self.students.remove(student)
        else:
            raise Exception("This subject is empty!")