from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def new_dest(request):
        return render(request, 'destination.html') 