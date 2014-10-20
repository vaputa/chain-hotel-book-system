# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderdetail', '0002_orderdetail_room_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='room_id',
            new_name='room',
        ),
    ]
