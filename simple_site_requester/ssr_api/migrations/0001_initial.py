# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-27 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('datetime_started', models.DateTimeField(auto_now_add=True)),
                ('datetime_ended', models.DateTimeField(null=True)),
                ('elapsed_time', models.FloatField(null=True)),
            ],
        ),
    ]
