# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogBase', '0002_dog_dogslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='typedog',
            name='typeSlug',
            field=models.CharField(default='slug', max_length=100),
            preserve_default=False,
        ),
    ]
