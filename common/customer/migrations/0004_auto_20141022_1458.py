# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_accountcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
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
        migrations.RemoveField(
            model_name='accountcode',
            name='customer',
        ),
        migrations.DeleteModel(
            name='AccountCode',
        ),
    ]
