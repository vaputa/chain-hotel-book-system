# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(serialize=False, primary_key=True)),
                ('room_type', models.CharField(max_length=20)),
                ('room_number', models.CharField(max_length=5)),
                ('max_capacity', models.IntegerField(default=0)),
                ('basic_price', models.IntegerField(default=0)),
                ('hotel', models.ForeignKey(to='hotel.HotelEntity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
