# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20150218_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
