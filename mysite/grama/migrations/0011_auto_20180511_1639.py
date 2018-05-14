# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grama', '0010_birthcertificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthcertificate',
            name='title',
            field=models.CharField(max_length=100, choices=[(1, 'Mr'), (2, 'Mrs')]),
        ),
    ]
