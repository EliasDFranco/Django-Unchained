from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HelloWorld(request, username):
    print(username)
    return HttpResponse("<h1>Hello Goodfellas, my name is Tony Soprano, i'm living in New Jersey %s </h1> " % username)

def index(request):
    return HttpResponse("Index page")

