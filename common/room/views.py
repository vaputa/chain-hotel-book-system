# -*- coding: cp936 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from common.hotel.models import HotelEntity, HotelEntityForm
from models import RoomForm, Room


def room_add(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.save()
    elif request.method == "GET":
        form = RoomForm()
    return render(request, 'room.html', {'action' : '/room/add/', 'form' : form})

def room_edit(request, id):
    if request.method == 'POST':
        room = Room.objects.get(room_id = id)
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            room = form.save()
            room.save()
    elif request.method == "GET":
            room = get_object_or_404(Room, room_id = id)
    form = RoomForm(instance = room)
    return render(request, 'room.html', {'action' : '/room/' + id + '/edit/','form' : form})
