from django.db import models
from django.forms import ModelForm
from django import forms

from common.hotel.models import HotelEntity

class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    credit = models.IntegerField(default = 0)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20)

    @staticmethod
    def contain_email(e):
        return Customer.objects.filter(email = e)

    @staticmethod
    def is_auth(e, p):
        return Customer.objects.filter(email = e, password = p)

class CustomerRegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'phone', 'password')
