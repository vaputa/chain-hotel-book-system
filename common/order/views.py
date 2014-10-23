import datetime
import time

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from common.orderdetail.models import OrderDetail
from common.customer.models import Customer
from common.room.models import Room
from models import Order

def new(request, id, begin, end):
    if request.session.get('uid', None) == None:
        return HttpResponseRedirect('/')
    customer = Customer.objects.get(customer_id = request.session['uid'])
    room = Room.objects.get(room_id = id)
    s = datetime.date(*(time.strptime(begin, '%Y-%m-%d')[0:3]))
    t = datetime.date(*(time.strptime(end, '%Y-%m-%d')[0:3]))
    order = Order(room = room, customer = customer, check_in = s, check_out = t, price = 0)
    order.price = (t - s).days * room.basic_price
    order.save()
    while s != t:
        od = OrderDetail(room = room, order = order, order_date = s)
        od.save()
        s = s + datetime.timedelta(1)
    return render(request, 'room.html', {})

def pay(request, id):
    if request.session.get('uid', None) == None:
        return HttpResponseRedirect('/')
    order = Order.objects.get(order_id = id)
    if order.status == 0:
        order.status = 1
        order.save()
        customer = Customer.objects.get(customer_id = request.session['uid'])
        customer.credit += order.price
        customer.save()
    return HttpResponseRedirect('/order/list')


def get(request, id):
    if request.session.get('uid', None) == None:
        return HttpResponseRedirect('/')
    order = Order.objects.get(order_id = id)
    return HttpResponseRedirect('/order/list')


def list(request):
    if request.session.get('uid', None) == None:
        return HttpResponseRedirect('/')
    uid = request.session['uid']
    orders = Order.objects.filter(customer_id = uid)
    return render(request, 'order_list_customer.html', {'orders': orders})

def cancel(request, id):
    order = Order.objects.get(order_id = id) 
    orderdetails = OrderDetail.objects.filter(order_id = id)
    orderdetails.update(status = -1)
    order.status = -1
    order.save()
    return HttpResponseRedirect('/order/list')