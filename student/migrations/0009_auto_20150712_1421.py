# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20150702_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='student.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
        ),
    ]
