# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='SitePage',
        ),
    ]