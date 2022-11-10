from django.http import HttpResponse
from django.shortcuts import render,redirect
from pathlib import Path
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request,'base.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html',{'form':form})

chat = premium =contact =my_properties = base 

