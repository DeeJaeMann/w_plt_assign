from django.shortcuts import render, get_object_or_404
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)

# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
    
    def post(self, request):
        data = request.data.copy()
        pending_subject = SubjectSerializer(data=data)
        if pending_subject.is_valid():
            pending_subject.save()
            return Response(pending_subject.data, status=HTTP_201_CREATED)
        return Response(pending_subject.errors, status=HTTP_400_BAD_REQUEST)

class A_subject(APIView):
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        return Response(SubjectSerializer(subject).data)
    
    def put(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        data = request.data.copy()
        update_subject = SubjectSerializer(subject, data=data, partial=True)
        if update_subject.is_valid():
            update_subject.save()
            return Response(update_subject.data, status=HTTP_200_OK)
        return Response(update_subject.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subject):
        subject_title = subject.title()
        subject = get_object_or_404(Subject, subject_name = subject_title)
        subject.delete()
        return Response(f"Deleted {subject_title}", status=HTTP_204_NO_CONTENT)
