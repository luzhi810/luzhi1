# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-16 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.CharField(max_length=3)),
                ('head_url', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]