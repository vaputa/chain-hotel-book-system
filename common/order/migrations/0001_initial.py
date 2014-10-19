# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('status', models.IntegerField()),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('room', models.ForeignKey(to='room.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
