# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20170610_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
