# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20141024_1024'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('comment_time', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('hotel', models.ForeignKey(to='hotel.HotelEntity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
