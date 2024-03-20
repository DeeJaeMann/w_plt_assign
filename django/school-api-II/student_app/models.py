from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(blank=True, unique=True)
    locker_number = models.IntegerField(unique=True, default=110)
    locker_combination = models.CharField(max_length=10, default="12-12-12")
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, int_number):
        self.locker_number = int_number
        self.save()

    def student_status(self, bool_status):
        self.good_student = bool_status
        self.save()