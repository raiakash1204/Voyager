#this file has been created by me to define views.
from django.http import HttpRequest
from django.shortcuts import render


def home(request):
    return render(request, "homepage/index.html")

def login(request):
    return render(request, "login/index.html")