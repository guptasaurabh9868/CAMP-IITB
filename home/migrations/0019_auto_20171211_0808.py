# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20171129_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shadowexpire',
            field=models.IntegerField(default=0),
        ),
    ]