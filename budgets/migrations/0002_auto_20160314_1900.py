# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='type',
        ),
        migrations.AddField(
            model_name='budget',
            name='type',
            field=models.IntegerField(choices=[(-1, 'Expense'), (1, 'Revenue')], default=-1),
        ),
    ]
