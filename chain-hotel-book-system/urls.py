from django.conf.urls import include, url
from django.contrib import admin

from common.hotel.views import hotel_add, hotel_edit, hotel_list, hotel_room_list
from common.customer.views import customer_register, login
from common.room.views import room_add, room_edit

urlpatterns = [
    url('^$', 'common.views.homepage'),
    url('^login/$', login),
    url('^hotel/add/$', hotel_add),
    url('^hotel/(?P<id>\d{0,4})/edit/$', hotel_edit),
    url('^hotel/list/$', hotel_list),
    url('^hotel/(?P<id>\d{0,4})/room/$', hotel_room_list),
    url('^room/add/$', room_add),
    url('^room/(?P<id>\d{0,4})/edit/$', room_edit),
    url('^customer/register/$', customer_register),
#    url(r'^admin/', include(admin.site.urls)),
]
