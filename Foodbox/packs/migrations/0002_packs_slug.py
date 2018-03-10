# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='packs',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]