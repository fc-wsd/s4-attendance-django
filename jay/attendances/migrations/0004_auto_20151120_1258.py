# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_attendance_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='students',
        ),
        migrations.AddField(
            model_name='attendance',
            name='students',
            field=models.OneToOneField(to='attendances.Student', default=1),
            preserve_default=False,
        ),
    ]
