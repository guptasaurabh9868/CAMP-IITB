# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20171128_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shadowexpire',
            field=models.IntegerField(default=0),
        ),
    ]