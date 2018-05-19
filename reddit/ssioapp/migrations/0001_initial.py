# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 10:21
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_body', models.CharField(max_length=2000)),
                ('blog_heading', models.CharField(max_length=200)),
                ('blog_images', models.FileField(upload_to='posts/blogs/%Y/%m/%d')),
                ('blog_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 19, 10, 21, 33, 673313))),
                ('blog_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=240)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssioapp.Blogs')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_comment', models.CharField(blank=True, max_length=240, null=True)),
                ('share_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('share_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ssioapp.Blogs')),
                ('share_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]