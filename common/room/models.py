from django.db import models
from django.forms import ModelForm
from django import forms

from common.hotel.models import HotelEntity

class Room(models.Model):
    room_id = models.AutoField(primary_key = True)
    hotel = models.ForeignKey(HotelEntity)
    room_type = models.CharField(max_length = 20)
    room_number = models.CharField(max_length = 5)
    max_capacity = models.IntegerField(default = 0)
    basic_price = models.IntegerField(default = 0)


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
