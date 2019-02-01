from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from login.models import UserProfile

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class EditProfilePicture(UserChangeForm):
    
    class Meta:
        model = UserProfile
        fields = ('image','user')