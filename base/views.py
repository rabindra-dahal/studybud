from django.shortcuts import render
from .models import Room

# Create your views here.
data = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn Phoenix'},
    {'id': 3, 'name': 'Lets learn Web Development'},
    ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context = { 'room': room}
    return render(request, 'base/room.html', context)