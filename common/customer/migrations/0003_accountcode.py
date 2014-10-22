# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20141019_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=32)),
                ('status', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
