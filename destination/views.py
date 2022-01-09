from django.shortcuts import render, redirect
from django.http import HttpResponse
from travello.models import Destination

# Create your views here.


def new_dest(request,city_name):
    # dests = Destination.objects.all().filter(name=city_name)
    dests = Destination.objects.all().filter(name=city_name)
    return render(request, 'destination.html',{'dests': dests})