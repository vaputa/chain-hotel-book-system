from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from models import Customer, CustomerRegisterForm

from common.models import LoginForm
from common.hotel.models import HotelEntity, HotelEntityForm

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
            #TODO
    form = CustomerRegisterForm()
    return render(request, 'register.html', {'form' : form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if not Customer.contain_email(email):
                return render(request, 'login.html', {'form' : form , 'non_exist_email' : True})
            elif not Customer.is_auth(email, password):
                return render(request, 'login.html', {'form' : form , 'wrong_password' : True})
            else:
                print "login successfully"
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})
