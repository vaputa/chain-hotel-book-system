from django.db import models
from django import forms

from common.customer.models import Customer
from common.room.models import Room

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_time = models.DateTimeField(auto_now = True)
    room = models.ForeignKey(Room)
    customer = models.ForeignKey(Customer)
    price = models.IntegerField()
    status = models.IntegerField(default = 0)

#class OrderForm(form.Forms):
