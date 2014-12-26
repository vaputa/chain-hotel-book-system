#-*-coding:utf-8-*- 
from django.db import models
from django.forms import ModelForm
from django import forms

class HotelEntity(models.Model):
    hotel_id = models.AutoField(primary_key = True);
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    tel = models.CharField(max_length = 20)
    location = models.CharField(max_length = 30)
    def __str__(self):
        return self.name


class HotelEntityForm(ModelForm):
    #hotel_id = forms.IntegerField(widget = forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='名称')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='地址')
    tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='电话')
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label='坐标')
    class Meta:
        model = HotelEntity
        fields = '__all__'
