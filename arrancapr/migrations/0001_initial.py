# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.models import Group


def create_default_groups(apps, schema_editor):
    instructors_group, _ = Group.objects.get_or_create(name='Instructors')
    students_group, _ = Group.objects.get_or_create(name='Students')

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunPython(create_default_groups),
    ]
