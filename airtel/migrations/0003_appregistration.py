

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-23 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtel', '0002_auto_20191022_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=13, null=True)),
                ('lastname', models.CharField(blank=True, max_length=13, null=True)),
                ('msisdn', models.CharField(blank=True, max_length=13, null=True)),
                ('createdDate', models.DateTimeField()),
                ('imeiNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('os', models.CharField(blank=True, max_length=20, null=True)),
                ('osVersion', models.CharField(blank=True, max_length=20, null=True)),
                ('lastLoginDate', models.DateTimeField()),
                ('isNew', models.NullBooleanField()),
                ('lob', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]