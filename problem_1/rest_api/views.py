from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for 'Student' model, all CRUD operations are available.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer