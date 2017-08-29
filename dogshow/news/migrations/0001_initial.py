# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('timefield', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
