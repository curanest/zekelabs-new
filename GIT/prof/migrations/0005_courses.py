# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_auto_20160919_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('trainer', models.CharField(max_length=20)),
                ('sme', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=2, choices=[(b'Micro', b'micro'), (b'Foundation', b'foundation'), (b'Advance', b'advance')])),
                ('content', models.TextField()),
                ('duration', models.CharField(max_length=10)),
                ('ongoing_batch', models.DateTimeField()),
                ('upcomming_batch', models.DateTimeField()),
            ],
        ),
    ]
