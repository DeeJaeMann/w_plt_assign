from django.shortcuts import render, get_object_or_404
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
    
class A_subject(APIView):
    def get(self, request, subject):
        subject=subject.title()
        subject = get_object_or_404(Subject, subject_name=subject)
        ser_subject = SubjectSerializer(subject)
        return Response(ser_subject.data)
