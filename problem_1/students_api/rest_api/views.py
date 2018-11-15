"""
@author  : Santiago Quiroga Turdera
@version : 1.0
"""

from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Class, Student
from .serializers import ClassSerializer, StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint for 'Class' model, all CRUD operations are supported.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('code', 'title', 'description', 'enrolled_students')


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for 'Student' model, all CRUD operations are supported.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name', 'enrolled_to')