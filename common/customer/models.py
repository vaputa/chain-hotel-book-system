#coding=utf-8
from django.db import models
from django.forms import ModelForm
from django import forms

from common.hotel.models import HotelEntity

class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    credit = models.IntegerField(default = 0)
    email = models.EmailField()
    name = models.CharField(max_length = 10, default=None)
    phone = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    status = models.IntegerField(default = 0)

    @staticmethod
    def contain_email(e):
        return Customer.objects.filter(email = e)

    @staticmethod
    def is_auth(e, p):
        return Customer.objects.filter(email = e, password = p)

class CustomerRegisterForm(ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = '姓名')
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = 'Email')
    password = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = '密码')
    phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = '手机号码')
    class Meta:
        model = Customer
        fields = ('name', 'email', 'password', 'phone')

class Token(models.Model):
    token = models.CharField(max_length = 32)
    customer = models.ForeignKey(Customer)
    status = models.IntegerField(default = 0)

