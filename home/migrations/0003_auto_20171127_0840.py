# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171101_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='roll_number',
            field=models.CharField(default='himanshu', max_length=20),
        ),
    ]
