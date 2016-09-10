# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160910_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='desc', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]