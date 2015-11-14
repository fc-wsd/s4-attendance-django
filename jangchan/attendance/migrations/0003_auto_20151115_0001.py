# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20151114_2359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='Lecture',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='subject',
            new_name='Lecture',
        ),
    ]
