# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20141020_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), (1, b'\xe5\xb7\xb2\xe6\x94\xaf\xe4\xbb\x98'), (2, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88'), (3, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
            preserve_default=True,
        ),
    ]
