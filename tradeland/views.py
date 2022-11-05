from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from django.urls import reverse, reverse_lazy


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request,'base.html')

chat = premium =contact =my_properties = base 

