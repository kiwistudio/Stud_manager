# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_journal', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='student.Student')),
            ],
            options={
                'verbose_name': '\u0416\u0443\u0440\u043d\u0430\u043b',
            },
        ),
    ]
