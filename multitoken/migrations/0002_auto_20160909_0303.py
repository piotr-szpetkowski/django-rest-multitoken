# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multitoken', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='token',
            unique_together=set([]),
        ),
    ]
