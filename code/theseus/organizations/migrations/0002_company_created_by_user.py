# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 01:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_by_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organizations_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
