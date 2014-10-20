# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20141019_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='check_in',
            field=models.DateTimeField(default=datetime.date(2014, 10, 21)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='check_out',
            field=models.DateTimeField(default=datetime.date(2014, 10, 24)),
            preserve_default=True,
        ),
    ]
