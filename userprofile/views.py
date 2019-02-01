from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.template import loader
from django.contrib.auth.forms import PasswordChangeForm
from userprofile.forms import EditProfileForm, EditProfilePicture
from django.contrib.auth import update_session_auth_hash

def profile_view(request):
    args = {'user': request.user}
    return render(request,'profile/profilePage.html')

def profile_edit(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST, instance =request.user)
        
        if form.is_valid():
            form.save()
            return redirect('/profile/view')
        
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'profile/editProfile.html', args)
    
def editPassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user =request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile/edit')
        else:
            return redirect('/profile/editPassword')
        
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'profile/editPassword.html', args)