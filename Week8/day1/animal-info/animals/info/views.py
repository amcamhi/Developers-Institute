from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def info(request):
    return HttpResponse('<h1> INFO </h1>')


def family(request):
    return HttpResponse('<h1> Family Table </h1>')


def animal(request):
    return HttpResponse('<h1> Animal Table </h1>')
