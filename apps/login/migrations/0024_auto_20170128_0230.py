# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_quote_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users'),
        ),
    ]