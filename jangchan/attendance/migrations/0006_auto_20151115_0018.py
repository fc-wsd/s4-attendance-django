# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20151115_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='is_late',
            new_name='is_attend',
        ),
    ]
