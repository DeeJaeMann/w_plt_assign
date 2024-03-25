from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Subject

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
    
class SubjectAllSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()

    class Meta:
        model = Subject
        exclude = ['id']

    def get_students(self, instance):
        students = instance.students.count()
        return students
    
    def get_grade_average(self, instance):
        grades = instance.grades.count()
        all_grades = instance.grades.all()
        total = sum([grd.grade for grd in all_grades])
        return round(total / grades, 2)