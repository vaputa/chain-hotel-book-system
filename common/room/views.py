from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from models import RoomForm, Room
from common.models import SearchForm
from common.hotel.models import HotelEntity, HotelEntityForm


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

def room_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s = form.cleaned_data['order_begin']
            t = form.cleaned_data['order_end']
            rooms = Room.objects.extra(select = {'isFree' : 
                "SELECT COUNT(*) FROM orderdetail_orderdetail \
                 WHERE room_id = room_room.room_id AND '" + 
                 str(s) + "' <= order_date AND order_date <= '" + str(t) + "'"})
            ctx = {'form': form, 'rooms' : rooms}
            ctx['begin'] = s
            ctx['end'] = t
            return render(request, 'homepage.html', ctx)
    elif request.method == 'GET':
        form = SearchForm()
    return render(request, 'homepage.html', {'form': form})
