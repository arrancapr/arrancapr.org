from school.models import Course, Workshop, CourseRegistration, WorkshopRegistration
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()
    class Meta:
        model = Course


class WorkshopSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()
    class Meta:
        model = Workshop


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration


class WorkshopRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopRegistration
