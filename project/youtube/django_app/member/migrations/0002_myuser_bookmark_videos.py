# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bookmark_videos',
            field=models.ManyToManyField(to='video.Video'),
        ),
    ]
