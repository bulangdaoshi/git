# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0002_auto_20180430_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('gr', '个人'), ('gx', '高校'), ('pxjg', '培训机构')], default='pxjg', max_length=20, verbose_name='培训类别'),
        ),
    ]