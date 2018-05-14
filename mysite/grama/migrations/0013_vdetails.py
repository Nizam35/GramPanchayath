# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0012_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='VDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('village', models.CharField(max_length=100, default='')),
                ('total_men', models.IntegerField()),
                ('total_ladies', models.IntegerField()),
                ('total_sc', models.IntegerField()),
                ('total_st', models.IntegerField()),
                ('total_Physical_Disabled', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'VDetails',
            },
        ),
    ]
