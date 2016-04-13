# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20160412_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b'},
        ),
        migrations.AddField(
            model_name='student',
            name='skype',
            field=models.CharField(default='', max_length=35),
            preserve_default=False,
        ),
    ]
