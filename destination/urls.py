from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('new_dest', views.new_dest, name='new_dest')
]