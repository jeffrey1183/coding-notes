from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello world!</h1>")

def brian(request):
    return HttpResponse("Hello Brian!")

def yuna(request):
    return HttpResponse("Hello Yuna!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")