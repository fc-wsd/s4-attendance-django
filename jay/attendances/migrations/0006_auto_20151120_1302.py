# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0005_auto_20151120_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='end_time',
            new_name='end_time_hour',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='start_time',
            new_name='start_time_hour',
        ),
    ]
