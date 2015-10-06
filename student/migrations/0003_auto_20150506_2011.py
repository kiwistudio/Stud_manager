# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20150506_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='tittle',
            new_name='title',
        ),
    ]
