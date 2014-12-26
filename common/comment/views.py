from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import Comment
from common.hotel.models import HotelEntity
from common.customer.models import Customer

def list(request, hotel_id):
    comments = Comment.objects.filter(hotel_id = hotel_id)
    hotel = HotelEntity.objects.get(hotel_id = hotel_id)

    return render(request, 'comment.html', {'comments' : comments, 'hotel': hotel})

def add(request, hotel_id):
    if request.session.get('user', None) == None:
        return HttpResponseRedirect('/')

    customer = Customer.objects.get(email = request.session['user'])
    hotel = HotelEntity.objects.get(hotel_id = hotel_id)

    if  request.method == 'GET':
        pass
    elif request.method == 'POST':
        content = request.POST['comment']
        comment = Comment(content = content, customer = customer, hotel = hotel)
        comment.save()

    return HttpResponseRedirect('/comment/list/' + hotel_id)
