from django.shortcuts import render
from .serializers import SubjectAllSerializer, Subject
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class All_subjects(APIView):

    def get(self, request):
        subjects = Subject.objects.all()
        ser_subjects = SubjectAllSerializer(subjects, many=True)
        return Response(ser_subjects.data)