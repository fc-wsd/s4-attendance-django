# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20151115_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Lecture',
            new_name='lecture',
        ),
    ]
