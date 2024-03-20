# Generated by Django 4.2.11 on 2024-03-20 17:28

from django.db import migrations, models
import student_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200, validators=[student_app.validators.validate_name]),
        ),
    ]
