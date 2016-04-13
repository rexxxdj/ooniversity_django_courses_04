# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160412_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '\u041a\u0443\u0440\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '\u041b\u0435\u043a\u0446\u0438\u044f', 'verbose_name_plural': '\u041b\u0435\u043a\u0446\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(verbose_name=b'\xe2\x84\x96\xd0\xbf.\xd0\xbf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
    ]
