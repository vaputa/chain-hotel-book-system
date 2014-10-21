from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context,Template 
from django.template.loader import get_template  

from models import RoomForm, Room
from common.models import SearchForm
from common.hotel.models import HotelEntity, HotelEntityForm


def add(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.save()
    elif request.method == "GET":
        form = RoomForm()
    return render(request, 'room.html', {'action' : '/room/add/', 'form' : form})

def list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms' : rooms})

def edit(request, id):
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

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s = form.cleaned_data['order_begin']
            t = form.cleaned_data['order_end']
            rooms = Room.objects.extra(select = {'is_free' : 
                "SELECT COUNT(*) FROM orderdetail_orderdetail \
                WHERE status = 0 and room_id = room_room.room_id AND '" + 
                str(s) + "' <= order_date AND order_date < '" + str(t) + "'"})

            buf = {}
            def f(x): 
                r = str(x.hotel_id) + ' ' + str(x.room_type)
                if x.is_free != 0 or r in buf:
                    return False     
                buf[r] = True
                return True
            rooms = filter(f, rooms)
            ctx = {'form': form, 'rooms' : rooms}
            ctx['begin'] = s
            ctx['end'] = t
            return render(request, 'homepage.html', ctx)
    elif request.method == 'GET':
        form = SearchForm()
    return render(request, 'homepage.html', {'form': form})
