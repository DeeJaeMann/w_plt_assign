from django.db import models
from django.core import validators as v
from subject_app.models import Subject
from student_app.models import Student

# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(decimal_places=2, max_digits=5, default=100, validators=[v.MinValueValidator(0), v.MaxValueValidator(100.0)])
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)