from django.shortcuts import render
from rest_framework import viewsets
from .models import Class, Student
from .serializers import ClassSerializer, StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint for 'Class' model, all CRUD operations are supported.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for 'Student' model, all CRUD operations are supported.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer