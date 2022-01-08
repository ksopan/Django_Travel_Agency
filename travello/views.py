from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):
    
## Old style manuall static dynamic content
    # dest1 = Destination()
    # dest1.name = 'Toronto'
    # dest1.desc = 'The City That Never Sleeps'
    # dest1.price = 800
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False
    # dest2 = Destination()
    # dest2.name = 'Vancouver'
    # dest2.desc = 'The City Close to Heart'
    # dest2.price = 900
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True
    # dest3 = Destination()
    # dest3.name = 'Calgary'
    # dest3.desc = 'The City Of Mountains'
    # dest3.price = 700
    # dest3.img = 'destination_8.jpg'
    # dest3.offer = False
    
    # dests = [dest1, dest2, dest3]
    
    dests = Destination.objects.all()
    
    return render(request,"index.html",{'dests': dests})