# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-19 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_content',
            field=models.CharField(max_length=1000),
        ),
    ]
