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
#    print datetime.date(time.strptime(begin, "%Y-%m-%d"))
    customer = Customer.objects.get(customer_id = 1)
    room = Room.objects.get(room_id = 1)
    order = Order(room = room, customer = customer, price = 0)
    order.save()
    s = datetime.date(*(time.strptime(begin, '%Y-%m-%d')[0:3]))
    t = datetime.date(*(time.strptime(end, '%Y-%m-%d')[0:3]))
    while s != t:
        od = OrderDetail(order = order, order_date = s)
        od.save()
        s = s + datetime.timedelta(1)
    return render(request, 'room.html', {})
