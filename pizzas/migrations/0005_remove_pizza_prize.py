# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_prize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='prize',
        ),
    ]