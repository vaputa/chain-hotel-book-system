from django.db import models
from django import forms
import datetime

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 20)

class SearchForm(forms.Form):
    capacity = forms.IntegerField(initial = 2)
    order_begin = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(1)))
    order_end = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(4)))