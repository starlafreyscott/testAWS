# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_auto_20170128_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='owner',
            field=models.ForeignKey(blank=True, max_length=75, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Users'),
        ),
    ]
