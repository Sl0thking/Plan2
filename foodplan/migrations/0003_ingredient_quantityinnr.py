# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0002_auto_20160429_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantityInNr',
            field=models.IntegerField(null=True),
        ),
    ]
