# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0006_courses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='level',
            field=models.CharField(max_length=10, choices=[(b'Micro', b'micro'), (b'Foundation', b'foundation'), (b'Advance', b'advance')]),
        ),
    ]
