# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码', 'verbose_name_plural': '邮箱验证码'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='上传图片'),
        ),
    ]
