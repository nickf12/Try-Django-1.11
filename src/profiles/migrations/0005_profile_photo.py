# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_activation_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
