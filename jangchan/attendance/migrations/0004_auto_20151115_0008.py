# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20151115_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='name',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='lecture',
            name='weeknumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
