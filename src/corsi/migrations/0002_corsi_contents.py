# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corsi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corsi',
            name='contents',
            field=models.TextField(default=django.utils.timezone.now, help_text='separate each item by comma'),
            preserve_default=False,
        ),
    ]
