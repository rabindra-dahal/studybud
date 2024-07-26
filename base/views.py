from django.shortcuts import render

# Create your views here.
data = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn Phoenix'},
    {'id': 3, 'name': 'Lets learn Web Development'},
    ]

def home(request):
    return render(request, 'home.html', {'rooms': data})

def rooms(request):
    return render(request, 'rooms.html')