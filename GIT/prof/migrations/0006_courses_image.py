# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0005_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True),
        ),
    ]
