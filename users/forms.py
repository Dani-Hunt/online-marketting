from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from earn.models import Withdraw


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(required = True, max_length='25')

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class Withdraw(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ['phone', 'amount']     