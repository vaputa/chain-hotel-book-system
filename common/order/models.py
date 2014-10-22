#-*-coding:utf-8-*- 
from django.db import models
from django import forms

from common.customer.models import Customer
from common.room.models import Room

import datetime

class Order(models.Model):
    STATUS_CODE = (
        (-1, '已取消'),
        (0, '待支付'),
        (1, '已支付'),
        (2, '已完成'),
    )
    order_id = models.AutoField(primary_key = True)
    order_time = models.DateTimeField(auto_now = True)
    room = models.ForeignKey(Room)
    customer = models.ForeignKey(Customer)
    price = models.IntegerField()
    status = models.IntegerField(default = 0, choices = STATUS_CODE)
    check_in = models.DateField()
    check_out = models.DateField()
