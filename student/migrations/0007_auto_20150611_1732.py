# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_exam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('last_name',), 'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438'},
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430', to='student.Student'),
        ),
    ]
