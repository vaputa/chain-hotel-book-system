from django.db import models
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 20)

