# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0006_auto_20180501_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('Due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('EMD', models.IntegerField(default=0)),
                ('DOC_Fee', models.IntegerField(default=0)),
                ('Notice_Type', models.CharField(max_length=100, default='NULL')),
                ('Authority_Type', models.CharField(max_length=100, default='NULL')),
                ('Product_Services', models.CharField(max_length=100, default='NULL')),
                ('Doc_Sale_Starts', models.DateTimeField(default=django.utils.timezone.now)),
                ('Doc_Sale_Ends', models.DateTimeField(default=django.utils.timezone.now)),
                ('Doc_Submit_Before', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
