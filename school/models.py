import datetime

from django.db import models
from django.conf import settings


class BroadcastPlatform(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    number_of_weeks = models.IntegerField(default=0)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='courses_teaching')
    broadcast_platform = models.ForeignKey(
        BroadcastPlatform, related_name='courses')
    starts_by = models.DateTimeField()
    duration = models.DurationField(default=datetime.timedelta(hours=1, minutes=15))

    def __unicode__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='workshops_teaching')
    broadcast_platform = models.ForeignKey(
        BroadcastPlatform, related_name='workshops')
    date = models.DateTimeField()
    duration = models.DurationField(default=datetime.timedelta(hours=1, minutes=15))

    def __unicode__(self):
        return self.name


class CourseRegistration(models.Model):
    course = models.ForeignKey(
        Course, related_name='course_registrations')
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='course_registrations')

    def __unicode__(self):
        return self.course.name + ' Registration for ' + self.student.username


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(
        Workshop, related_name='workshop_registrations')
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='workshop_registrations')

    def __unicode__(self):
        return self.workshop.name + ' Registration for ' + self.student.username
