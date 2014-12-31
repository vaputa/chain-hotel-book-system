#-*-coding:utf-8-*-
from django.db import models
from django import forms

from common.hotel.models import HotelEntity
from common.customer.models import Customer

class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer)
    hotel = models.ForeignKey(HotelEntity)
    content = models.CharField(max_length = 200)
    comment_time = models.DateTimeField(auto_now = True)

