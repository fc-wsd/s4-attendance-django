# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0002_auto_20151120_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='students',
            field=models.ManyToManyField(to='attendances.Student'),
        ),
    ]
