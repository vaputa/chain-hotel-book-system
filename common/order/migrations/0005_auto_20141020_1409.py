# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20141020_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='check_in',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='check_out',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
