from django.http import request
from django.shortcuts import render
from users.forms import Withdraw
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'earn/home.html')

@login_required
def withdraw(request):
    w_form = Withdraw(instance=request.user)

    context = {
        'w_form' : w_form
    }
    return render(request, 'earn/withdraw.html', context)    

