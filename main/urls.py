from django.contrib import admin
from django.urls import path
from.views import*

urlpatterns = [
    path("index22/" ,index22, name='index22'),
]
