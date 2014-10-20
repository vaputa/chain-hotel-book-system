from django.conf.urls import include, url
from django.contrib import admin

from common.hotel.views import hotel_add, hotel_edit, hotel_list, hotel_room_list
from common.customer.views import customer_register, customer_edit, login, logout
from common.room.views import room_add, room_edit, room_search, room_list
from common.order.views import new_order, order_list

urlpatterns = [
    url('^$', 'common.views.homepage'),
    url('^login/$', login),
    url('^logout/$', logout),
    url('^hotel/add/$', hotel_add),
    url('^hotel/(?P<id>\d{0,4})/edit/$', hotel_edit),
    url('^hotel/list/$', hotel_list),
    url('^hotel/(?P<id>\d{0,4})/room/$', hotel_room_list),
    url('^room/add/$', room_add),
    url('^room/(?P<id>\d{0,4})/edit/$', room_edit),
    url('^room/search/$', room_search),
    url('^room/list/$', room_list),
    url('^order/list/$', order_list),
    url('^order/new_order/(?P<id>\d{0,4})/(?P<begin>(\d|-){0,12})/(?P<end>(\d|-){0,12})/$', new_order),
    url('^customer/register/$', customer_register),
    url('^customer/edit/$', customer_edit)
#    url(r'^admin/', include(admin.site.urls)),
]
