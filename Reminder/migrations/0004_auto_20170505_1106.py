# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder', '0003_auto_20170505_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
