from django.http import HttpResponse
from django.shortcuts import render,redirect
from pathlib import Path
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm,profile_register_form
from django.contrib.auth import login,logout,authenticate

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request,'base.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        pform = profile_register_form(request.POST)
        if form.is_valid() and pform.is_valid():
            user = form.save()
            user.refresh_from_db()
            pform=profile_register_form(request.POST,instance=user.profile)
            pform.full_clean()
            pform.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
        pform = profile_register_form()
    return render(request, 'registration/sign_up.html',{'form':form,'pform':pform})

chat = premium =contact =my_properties = base 

