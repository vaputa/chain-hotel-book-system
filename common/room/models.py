#encoding=utf8
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
    hotel = forms.ModelChoiceField(queryset=HotelEntity.objects,widget=forms.Select(attrs={'class': 'form-control', 'type': 'text'}),label='酒店名称')
    room_type =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='房间类型')
    room_number =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='房间号')
    max_capacity =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='人数')
    basic_price =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='价格')
    class Meta:
        model = Room
        fields = '__all__'
