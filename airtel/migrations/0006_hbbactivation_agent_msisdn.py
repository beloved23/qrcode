# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-27 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtel', '0005_auto_20191227_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='hbbactivation',
            name='agent_msisdn',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
