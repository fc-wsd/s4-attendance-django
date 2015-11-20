# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='checked_in',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 4, 0, 27, 197786, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
