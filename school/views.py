from rest_framework import viewsets
from school.models import (
    Course, Workshop, CourseRegistration,
    WorkshopRegistration)
from school.serializers import (
    CourseSerializer, WorkshopSerializer,
    CourseRegistrationSerializer,
    WorkshopRegistrationSerializer)



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class CourseRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer


class WorkshopRegistrationViewSet(viewsets.ModelViewSet):
    queryset = WorkshopRegistration.objects.all()
    serializer_class = WorkshopRegistrationSerializer
