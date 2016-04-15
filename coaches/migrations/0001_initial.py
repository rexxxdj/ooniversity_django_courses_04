# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female')])),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440\u044b',
            },
            bases=(models.Model,),
        ),
    ]
