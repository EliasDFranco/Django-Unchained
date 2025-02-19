from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HelloWorld(request):
    return HttpResponse("<h1>Hello Goodfellas, my name is Tony Soprano, i'm living in New Jersey</h1>")

