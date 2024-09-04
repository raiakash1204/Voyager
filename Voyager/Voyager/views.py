#this file has been created by me to define views.
from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request, "navigation/index.html")

def home(request):
    return render(request, "homepage/index.html")

def login(request):
    return render(request, "login/index.html")

def admin_login(request):
    return render(request, "admin_login/index.html")

def registration(request):
    return render(request, "registration/index.html")