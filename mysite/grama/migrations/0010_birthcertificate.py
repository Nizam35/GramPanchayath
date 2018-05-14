# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0009_auto_20180506_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('issue_Date', models.DateField(default=django.utils.timezone.now)),
                ('id_Card_No', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=255)),
                ('phone_number', models.CharField(max_length=17, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('childName', models.CharField(max_length=100)),
                ('Place_Of_Birth', models.CharField(max_length=100)),
                ('Date_Of_Birth', models.DateField(default=django.utils.timezone.now)),
                ('fatherName', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=100)),
                ('ID_card_no_child', models.CharField(max_length=100)),
            ],
        ),
    ]
