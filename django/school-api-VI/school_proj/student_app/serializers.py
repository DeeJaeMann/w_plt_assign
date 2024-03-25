from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student
from subject_app.serializers import SubjectAllSerializer, Subject


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

        ser_subjects = SubjectAllSerializer(subjects, many=True)

        return ser_subjects.data