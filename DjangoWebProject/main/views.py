from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title' : 'Esta',
        'values' : ['Temperature: 21', 'Humidity: 21%', 'Time: 12:00'],
        'obj' : {
            '123' : 'ha',
            '2345' : 'no'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def panel(request):
    return render(request, 'main/panel.html')