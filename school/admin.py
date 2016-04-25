from django.contrib import admin
from school.models import (
    Course, Workshop, BroadcastPlatform,
    CourseRegistration, WorkshopRegistration)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(BroadcastPlatform)
class BroadcastPlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass
