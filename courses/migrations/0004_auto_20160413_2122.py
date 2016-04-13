# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160413_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={},
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
