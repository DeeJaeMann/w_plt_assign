# Generated by Django 4.2.11 on 2024-03-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=50, unique=True)),
                ('personal_email', models.EmailField(blank=True, max_length=50, unique=True)),
                ('locker_number', models.IntegerField(default=110, unique=True)),
                ('locker_combination', models.CharField(default='12-12-12', max_length=10)),
                ('good_student', models.BooleanField(default=True)),
            ],
        ),
    ]