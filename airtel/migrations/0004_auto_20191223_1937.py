# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-23 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtel', '0003_appregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appregistration',
            name='createdDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appregistration',
            name='lastLoginDate',
            field=models.DateTimeField(null=True),
        )
    ]
