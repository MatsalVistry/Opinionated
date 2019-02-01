from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template import loader
from login.forms import RegistrationForm

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/loginpage')
    else:
        form = RegistrationForm()
    return render(request,'login/signup.html',{'form':form})

def loginpage_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/politics')
    else:
        form=AuthenticationForm()
    return render(request,'login/loginpage.html',{'form':form})