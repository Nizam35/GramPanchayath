# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0014_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
