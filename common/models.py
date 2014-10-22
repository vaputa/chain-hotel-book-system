#coding=utf-8
from django.db import models
from django import forms
import datetime

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 20)

class SearchForm(forms.Form):
    capacity = forms.IntegerField(initial = 2, widget=forms.NumberInput(attrs={'class': 'form-control'}), label='人数')
    order_begin = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(1)), widget=forms.TextInput(attrs={'class': 'form-control'}), label='入住日期')
    order_end = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(4)), widget=forms.TextInput(attrs={'class': 'form-control'}), label='离店日期')