# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('patronymic', models.CharField(max_length=35)),
                ('rating', models.IntegerField()),
                ('package', models.CharField(max_length=35)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('skype', models.CharField(max_length=35)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
