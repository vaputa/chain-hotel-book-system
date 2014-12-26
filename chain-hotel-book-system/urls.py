from django.conf.urls import include, url
from django.contrib import admin

from common.customer.views import login, logout

urlpatterns = [
    url('^$', 'common.views.homepage'),
    url('^login/$', login),
    url('^logout/$', logout),
    url('^hotel/add/$', 'common.hotel.views.add'),
    url('^hotel/(?P<id>\d{0,6})/edit/$', 'common.hotel.views.edit'),
    url('^hotel/list/$', 'common.hotel.views.list'),
    url('^hotel/(?P<id>\d{0,6})/room/$', 'common.hotel.views.room_list'),
    url('^room/add/$', 'common.room.views.add'),
    url('^room/(?P<id>\d{0,6})/edit/$', 'common.room.views.edit'),
    url('^room/search/$', 'common.room.views.search'),
    url('^room/list/$', 'common.room.views.list'),
    url('^order/list/$', 'common.order.views.list'),
    url('^order/pay/(?P<id>\d{0,6})$', 'common.order.views.pay'),
    url('^order/get/(?P<id>\d{0,6})/$', 'common.order.views.get'),
    url('^order/cancel/(?P<id>\d{0,6})/$', 'common.order.views.cancel'),
    url('^order/new_order/(?P<id>\d{0,6})/(?P<begin>(\d|-){0,12})/(?P<end>(\d|-){0,12})/$', 'common.order.views.new'),
    url('^customer/register/$', 'common.customer.views.register'),
    url('^customer/edit/$', 'common.customer.views.edit'),
    url('^customer/profile/$', 'common.customer.views.profile'),
    url('^account/(?P<token>[\d\w]{32})/$', 'common.customer.views.account_service'),
    url('^comment/list/(?P<hotel_id>\d{0,6})/$', 'common.comment.views.list'),
    url('^comment/add/(?P<hotel_id>\d{0,6})/$', 'common.comment.views.add'),
    url('^api/json/order/(?P<uid>\d{0,6})/$', 'common.order.views.order_api'),
    url('^api/json/auth/', 'common.customer.views.login_api')
#    url(r'^admin/', include(admin.site.urls)),
]
