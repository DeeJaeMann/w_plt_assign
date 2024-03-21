from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email, validate_combination_format

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_name])
    student_email = models.EmailField(max_length=50, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=50, blank=True, unique=True)
    locker_number = models.IntegerField(unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=10, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_assignement(self, int_locker_number):
        self.locker_number = int_locker_number
        self.save()

    def student_status(self, bool_status):
        self.good_student = bool_status
        self.save()