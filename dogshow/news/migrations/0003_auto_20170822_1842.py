# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170822_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='NewsImages'),
        ),
    ]
