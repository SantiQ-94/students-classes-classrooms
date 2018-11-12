from django.test import TestCase
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student, Class


class ClassTest(APITestCase):
    def test_create_a_class(self):
        """
        Create a simple class instance of 'Class' model, and inspect its attributes.
        """

        data = {
            'code': 'CS101',
            'title': 'Introduction to Programming',
            'description': 'This is a basic yet exciting course',
            'enrolled_students':[]
        }
        url = reverse('class-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Class.objects.count(), 1)
        self.assertEqual(Class.objects.get().code, 'CS101')
        self.assertEqual(Class.objects.get().title, 'Introduction to Programming')
        self.assertEqual(Class.objects.get().description, 'This is a basic yet exciting course')


class StudentTest(APITestCase):
    
    def test_create_a_student(self):
        """
        Create a single instance of 'User' model and inspect its attributes.
        """
        data_class = {
            'code': 'CS101',
            'title': 'Introduction to Programming',
            'description': 'This is a basic yet exciting course',
            'enrolled_students':[]
        }
        url_class = reverse('class-list')
        response_class = self.client.post(url_class, data_class, format='json')
        self.assertEqual(response_class.status_code, status.HTTP_201_CREATED)
        class_pk = Class.objects.get().pk

        data = {
            'first_name': 'Santiago',
            'last_name': 'Quiroga Turdera',
            'enrolled_to': ['http://127.0.0.1:8000' + reverse('class-detail', kwargs={'pk':class_pk}),]
        }
        url = reverse('student-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, 'Santiago')
        self.assertEqual(Student.objects.get().last_name, 'Quiroga Turdera')
        self.assertEqual(Student.objects.get().enrolled_to.count(), 1)
        self.assertEqual(Student.objects.get().enrolled_to.get().code, 'CS101')

