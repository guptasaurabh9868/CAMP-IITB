# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20171129_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shadowexpire',
            field=models.CharField(max_length=20),
        ),
    ]
