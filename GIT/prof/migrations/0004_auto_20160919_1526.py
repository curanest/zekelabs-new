# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_auto_20160918_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerprofile',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]
