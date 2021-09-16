from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile
from earn.models import Withdraw, Quiz, Quiz1, Pat


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

class Quiz(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['firstname','lastname','age','gender','phone','id_number']        

class Quiz1(forms.ModelForm):
    class Meta:
        model = Quiz1
        fields = ['location','name','like','rate','dislike','rules']          


            # 'Where do you live',
            # 'What is the name of this plattform',
            # 'Do you like this plattform',
            # 'On a scale of 1-10 rate this plattform',
            # 'What do you dislike about this plattform',
            # 'Do you agree to abide by the rules of this plattform'

class Pat(forms.ModelForm):
    class Meta:
        model = Pat
        fields = ['pattern']
