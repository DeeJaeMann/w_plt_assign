from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    student_email = models.EmailField()
    personal_email = models.EmailField(blank=True)
    locker_number = models.IntegerField()
    locker_combination = models.CharField(max_length=10)
    good_student = models.BooleanField(default=True)