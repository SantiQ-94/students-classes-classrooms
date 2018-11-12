from django.db import models


class Class(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70)
    enrolled_to = models.ManyToManyField(Class, null=True, blank=True, related_name='enrolled_students')