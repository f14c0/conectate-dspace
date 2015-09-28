# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('handle', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=500)),
                ('license', models.CharField(max_length=30)),
                ('copyrightText', models.CharField(max_length=500)),
                ('introductoryText', models.CharField(max_length=500)),
                ('shortDescription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('handle', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=500)),
                ('license', models.CharField(max_length=30)),
                ('copyrightText', models.CharField(max_length=500)),
                ('introductoryText', models.CharField(max_length=500)),
                ('parentCommunity', models.ForeignKey(to='api.Community')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('handle', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=500)),
                ('parentCollection', models.ForeignKey(to='api.Collection')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='parentCommunity',
            field=models.ForeignKey(to='api.Community'),
        ),
    ]
