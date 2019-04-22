# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-22 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HandyHelper', '0003_auto_20190422_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_list',
        ),
        migrations.AddField(
            model_name='task',
            name='users_task_list',
            field=models.ManyToManyField(related_name='task_list', to='HandyHelper.User'),
        ),
    ]
