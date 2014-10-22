#-*-coding:utf-8-*- 
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from models import Customer, Token, CustomerRegisterForm

from common import utility
from common.models import LoginForm
from common.hotel.models import HotelEntity, HotelEntityForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
            token = Token(token = utility.generate_token(), customer = customer)
            token.save()
            content = '''<!DOCTYPE HTML><html><head><meta charset="utf-8"><title>Guo Hao Hotel注册验证</title></head><body><a href='localhost:8000/account/%s/'>激活</a></body></html>'''
            utility.send_mail(customer.email, 'GuoHaoHotel', content % token.token)
            return render(request, 'info.html', {'info': '已经发送一封邮件至%s，请点击连接激活账户' % customer.email})

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

def edit(request):
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

def account_service(request, token):
    token_object = get_object_or_404(Token, token = token)
    customer = token_object.customer
    customer.status = 1
    customer.save()
    token_object.status = 1
    token_object.save()
    return render(request, 'info.html', {'info' : "验证成功"})