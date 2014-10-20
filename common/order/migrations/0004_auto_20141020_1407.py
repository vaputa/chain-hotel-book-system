# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20141020_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='check_in',
            field=models.DateField(default=datetime.date(2014, 10, 21)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='check_out',
            field=models.DateField(default=datetime.date(2014, 10, 24)),
            preserve_default=True,
        ),
    ]
