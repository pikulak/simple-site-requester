# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-26 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssr_api', '0003_auto_20170926_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siterequest',
            name='datetime_ended',
            field=models.DateTimeField(null=True),
        ),
    ]