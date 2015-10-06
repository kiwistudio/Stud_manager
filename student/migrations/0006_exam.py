# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('time_of_act', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('lecturer', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0430')),
                ('exam_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='student.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0456\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0456\u0441\u043f\u0438\u0442\u0438',
            },
        ),
    ]
