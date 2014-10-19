from django.db import models

from common.room.models import Room


class OrderDetail(models.Model):    
    room = models.ForeignKey(Room)
    order_date = models.DateField()
    