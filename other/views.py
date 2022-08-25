from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def simple(request):
    return HttpResponse("hello")