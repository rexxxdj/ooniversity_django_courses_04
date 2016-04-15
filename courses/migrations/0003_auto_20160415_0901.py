# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0002_auto_20160413_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '\u041a\u0443\u0440\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': '\u0423\u0440\u043e\u043a\u0438'},
        ),
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name=b'assistant_courses', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name=b'coach_courses', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
