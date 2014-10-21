from django.db import models

from common.order.models import Order
from common.room.models import Room

class OrderDetail(models.Model):  
    order = models.ForeignKey(Order)
    room = models.ForeignKey(Room)  
    order_date = models.DateField()
    status = models.IntegerField(default = 0)