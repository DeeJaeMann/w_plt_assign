from rest_framework import serializers
from .models import Student
from subject_app.serializers import SubjectSerializer

#TODO: Refactor repeatitive code

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        exclude = ['id']

        def get_subjects(self, instance):
            return SubjectSerializer(instance.students.all(), many=True).data
