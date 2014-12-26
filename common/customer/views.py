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
    info = ''
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Customer.objects.filter(email= email).count() == 0:
                customer = form.save()
                customer.save()
                token = Token(token = utility.generate_token(), customer = customer)
                token.save()
                content = '''<!DOCTYPE HTML><html><head><meta charset="utf-8"><title>Guo Hao Hotel注册验证</title></head><body><a href='localhost:8000/account/%s/'>激活</a></body></html>'''
                utility.send_mail(customer.email, 'GuoHaoHotel', content % token.token)
                info = '已经发送一封邮件至%s，请点击链接激活账户' % customer.email
            else:
                info = '邮箱已经注册！'
    elif request.method == 'GET':
        form = CustomerRegisterForm()
    return render(request, 'register.html', {'form' : form, 'info' : info})

def login(request):
    info = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if email == 'admin@hotel.com':
                if password == 'password':
                    request.session['is_admin'] = True
                    request.session['uid'] = '-1'
                    request.session['user'] = 'HotelAdmin'
                    info = '登陆成功'
                else :
                    info = '密码错误！'
            elif not Customer.contain_email(email):
                info = 'EMAIL不存在！'
            elif not Customer.is_auth(email, password):
                info = '密码错误！'
            else:
                customer = Customer.objects.get(email = email)
                request.session['is_admin'] = False
                request.session['uid'] = customer.customer_id
                request.session['user'] = email
                info = '登录成功'
    form = LoginForm()
    return render(request, 'login.html', {'form' : form, 'info' : info})

def logout(request):
    del request.session['user']
    del request.session['uid']
    del request.session['is_admin']
    return HttpResponseRedirect("/")

def edit(request):
    info = ''
    if request.session.get('user', None) == None:
        return HttpResponseRedirect('/')
    customer = Customer.objects.get(email = request.session['user'])
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST, instance = customer)
        if form.is_valid():
            customer = form.save()
            customer.save()
            info = '更新成功！'
    else:
        form = CustomerRegisterForm(instance = customer)
    return render(request, 'customer_edit.html', {'form' : form, 'info' : info})

def account_service(request, token):
    token_object = get_object_or_404(Token, token = token)
    customer = token_object.customer
    customer.status = 1
    customer.save()
    token_object.status = 1
    token_object.save()
    return render(request, 'info.html', {'info' : "验证成功"})

def profile(request):
    if request.session.get('user', None) == None:
        return HttpResponseRedirect('/')
    customer = Customer.objects.get(email = request.session['user'])
    return render(request, 'profile.html', {'customer' : customer})

def login_api(request):
    info = ''
    status_code = -1
    customer = None
    if request.method == "GET":
        form = request.GET
        email = form['email']
        password = form['password']            
        if not Customer.contain_email(email):
            status_code = 1
        elif not Customer.is_auth(email, password):
            status_code = 2
        else:
            customer = Customer.objects.get(email = email)
            status_code = 0
    return render(request, 'auth.json', {'status_code' : status_code, 'customer' : customer})
