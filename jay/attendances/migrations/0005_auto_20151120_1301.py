# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0004_auto_20151120_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='created_at',
            new_name='attendance_datetime',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='endHourTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='startHourTime',
            new_name='start_time',
        ),
    ]
