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
    print "current user: " + str(request.session.get('user', None))
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
                customer = Customer.objects.get(email = email)
                request.session['uid'] = customer.customer_id
                request.session['user'] = email
                print "login successfully"
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def logout(request):
    del request.session['user']
    del request.session['uid']
    return HttpResponseRedirect("/")

def customer_edit(request):
    if request.session.get('user', None) == None:
        return HttpResponseRedirect('/')
    customer = Customer.objects.get(email = request.session['user'])
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST, instance = customer)
        if form.is_valid():
            customer = form.save()
            customer.save()
    else:
        form = CustomerRegisterForm(instance = customer)
    return render(request, 'customer_edit.html', {'form' : form})