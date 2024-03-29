# Generated by Django 5.0.3 on 2024-03-22 18:26

import subject_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professor',
            field=models.CharField(default='Mr. Cahan', max_length=100, validators=[subject_app.validators.validate_professor_name]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, unique=True, validators=[subject_app.validators.validate_subject_format]),
        ),
    ]
