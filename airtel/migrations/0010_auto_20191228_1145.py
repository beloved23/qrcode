# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-28 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtel', '0009_auto_20191228_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='msisdn',
            field=models.CharField(max_length=10),
        ),
    ]
