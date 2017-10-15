# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('ram', models.IntegerField(default=0)),
                ('console', models.IntegerField(default=0)),
                ('image', models.IntegerField(default=0)),
                ('path', models.TextField(default='')),
                ('start_script', models.TextField(default='')),
                ('stop_script', models.TextField(default='')),
                ('ip', models.TextField(default='')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='instance',
            unique_together=set([('name', 'path')]),
        ),
    ]
