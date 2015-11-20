# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0006_auto_20151120_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='students',
            new_name='student',
        ),
    ]
