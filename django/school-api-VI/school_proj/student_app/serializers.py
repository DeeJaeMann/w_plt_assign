from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number"]


class StudentAllSerializer(ModelSerializer):
    subjects = SerializerMethodField()

    class Meta:
        model = Student
        exclude = ['id']

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        ser_subjects = [{'subject_name':sub.subject_name, 'professor':sub.professor} for sub in subjects]
        return ser_subjects