from django.test import TestCase
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentTest(APITestCase):
    
    def test_create_a_student(self):
        """
        Create a single instance of 'User' model and inspect its attributes.
        """
        
        data = {
            'first_name': 'Santiago',
            'last_name': 'Quiroga Turdera'
        }
        url = reverse('student-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, 'Santiago')
        self.assertEqual(Student.objects.get().last_name, 'Quiroga Turdera')

