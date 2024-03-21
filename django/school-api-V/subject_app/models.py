from django.db import models
from django.core import validators as v
# from .validators import

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)
    professor = models.CharField(max_length=100, default="Mr. Cahan")