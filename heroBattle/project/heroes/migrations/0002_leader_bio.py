# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='bio',
            field=models.TextField(default='blank', max_length=500),
        ),
    ]
