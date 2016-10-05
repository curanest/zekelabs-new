# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_userprofile_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
