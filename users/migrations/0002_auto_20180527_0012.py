# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_image',
            field=models.ImageField(upload_to='static/user_images'),
        ),
    ]