from django.conf.urls import url, include

from rest_framework import routers
from school.views import (
    CourseViewSet, WorkshopViewSet,
    CourseRegistrationViewSet,
    WorkshopRegistrationViewSet)


router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'course_registrations', CourseRegistrationViewSet)
router.register(r'workshop_registrations', WorkshopRegistrationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
