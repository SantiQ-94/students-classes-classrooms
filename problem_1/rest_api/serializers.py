from rest_framework import serializers
from .models import Class, Student 



class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ('code', 'title', 'description', 'enrolled_students')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    enrolled = ClassSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = '__all__'
