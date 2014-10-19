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
        return self.name + self.address + self.tel


class HotelEntityForm(ModelForm):
    #hotel_id = forms.IntegerField(widget = forms.HiddenInput)
    class Meta:
        model = HotelEntity
        fields = '__all__'
