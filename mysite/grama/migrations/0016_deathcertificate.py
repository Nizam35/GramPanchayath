# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0015_feedback_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeathCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('issue_Date', models.DateField(default=django.utils.timezone.now)),
                ('Sex', models.CharField(max_length=100, choices=[(1, 'Male'), (2, 'Female')])),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=255)),
                ('phone_number', models.CharField(max_length=17, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('Date_of_Death', models.DateField(default=django.utils.timezone.now)),
                ('Place_of_Death', models.CharField(max_length=100)),
                ('Place_Of_Birth', models.CharField(max_length=100)),
                ('Date_Of_Birth', models.DateField(default=django.utils.timezone.now)),
                ('fatherName', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=100)),
                ('adharcard_no', models.CharField(max_length=100)),
            ],
        ),
    ]
