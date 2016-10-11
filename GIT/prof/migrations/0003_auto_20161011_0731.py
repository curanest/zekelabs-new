# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_courses_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='rating_average',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='rating_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='rating_sum',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]