from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

import datetime
import time

from common.orderdetail.models import OrderDetail
from common.customer.models import Customer
from common.room.models import Room
from models import Order

def new_order(request, id, begin, end):
    customer = Customer.objects.get(customer_id = 1) #TODO
    room = Room.objects.get(room_id = id)
    s = datetime.date(*(time.strptime(begin, '%Y-%m-%d')[0:3]))
    t = datetime.date(*(time.strptime(end, '%Y-%m-%d')[0:3]))

    order = Order(room = room, customer = customer, check_in = s, check_out = t, price = 0)
    order.save()
    while s != t:
        od = OrderDetail(room = room, order = order, order_date = s)
        od.save()
        s = s + datetime.timedelta(1)
    return render(request, 'room.html', {})

def order_list(request):
    if request.session.get('uid', None) == None:
        return HttpResponseRedirect('/')
    uid = request.session['uid']
    orders = Order.objects.filter(customer_id = uid)
    print orders
    return render(request, 'order_list_customer.html', {'orders': orders})
