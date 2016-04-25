# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 02:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0006_auto_20160320_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('obsolete', models.BooleanField(default=False)),
                ('duration', models.DurationField(default=datetime.timedelta(0, 4500))),
                ('broadcast_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='school.BroadcastPlatform')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops_teaching', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'obsolete'],
            },
        ),
    ]