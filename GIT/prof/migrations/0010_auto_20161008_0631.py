# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0009_courses_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
