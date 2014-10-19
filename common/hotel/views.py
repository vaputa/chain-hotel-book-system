from django.shortcuts import render

# -*- coding: cp936 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from models import HotelEntity, HotelEntityForm
from common.room.models import Room

def hotel_add(request):
    if request.method == 'POST':
        form = HotelEntityForm(request.POST)
        if form.is_valid():
            hotel_entity = form.save()
            hotel_entity.save()
    else:
        form = HotelEntityForm()
    return render(request, 'hotel.html', {'action': '/hotel/add/', 'form' : form})   

def hotel_edit(request, id):
    if request.method == 'POST':
        hotel_entity = HotelEntity.objects.get(hotel_id = id)
        form = HotelEntityForm(request.POST, instance = hotel_entity)
        if form.is_valid():
            hotel_entity = form.save()
            hotel_entity.save()
    else:
        hotel_entity = get_object_or_404(HotelEntity, hotel_id = id)

    form = HotelEntityForm(instance = hotel_entity)
    return render(request, 'hotel.html', {'action': '/hotel/' + id +'/edit/','form' : form})

def hotel_list(request):
    hotels = HotelEntity.objects.all()
    return render(request, 'hotels.html', {'hotels' : hotels})

def hotel_room_list(request, id):
    rooms = Room.objects.filter(hotel_id = id)
    return render(request, 'rooms.html', {'rooms' : rooms})
