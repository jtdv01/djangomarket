# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160910_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug-field'),
        ),
    ]
