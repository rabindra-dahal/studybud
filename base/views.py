from django.shortcuts import render

# Create your views here.
data = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn Phoenix'},
    {'id': 3, 'name': 'Lets learn Web Development'},
    ]

def home(request):
    context = {'rooms': data}
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    room = None
    for i in data:
        if i['id'] == int(pk):
            room = i
    context = { 'room': room}
    return render(request, 'base/room.html', context)