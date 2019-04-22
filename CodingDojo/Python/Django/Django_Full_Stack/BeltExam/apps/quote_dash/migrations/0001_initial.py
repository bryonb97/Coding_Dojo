# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-21 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_content', models.CharField(max_length=1000)),
                ('quote_author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_like',
            field=models.ManyToManyField(related_name='user_likes', to='quote_dash.User'),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quote', to='quote_dash.User'),
        ),
    ]