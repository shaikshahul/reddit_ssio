# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 10:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 19, 10, 23, 7, 983778)),
        ),
    ]