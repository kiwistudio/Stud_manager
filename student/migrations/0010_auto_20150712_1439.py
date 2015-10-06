# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20150712_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='lecturer',
            field=models.CharField(max_length=256, verbose_name='\u0438\u043c\u2019\u044f \u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0430'),
        ),
    ]
