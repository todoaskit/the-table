# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grapp', '0011_candidate_color_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='shadow_class',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
