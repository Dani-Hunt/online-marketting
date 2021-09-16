from django.http import request
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import Withdraw, Quiz , Quiz1, Pat
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


def quiz(request):
  if request.method == 'POST' :
    s_form = Quiz(request.POST, instance=request.user)
 
    if s_form.is_valid():
        s_form.save()
        messages.success(request, f'Succcess')
        return redirect('quiz1')

  else:
        s_form = Quiz(instance=request.user)
        context = {
                    's_form' : s_form,
                }
  return render(request, 'earn/quiz.html',context)


def quiz1(request):
  if request.method == 'POST' :
    s1_form = Quiz1(request.POST, instance=request.user)
 
    if s1_form.is_valid():
            s1_form.save()
            messages.success(request, f'Succcess')
            return redirect('credit')

  else:
    s1_form = Quiz1(instance=request.user)

    context = {
        's1_form' : s1_form,
    }
    return render(request, 'earn/quiz1.html',context)


def treasure(request):
    return render(request, 'earn/treasure.html')


@login_required
def credit(request):
    return render(request, 'earn/credit.html')

    

@login_required
def spin(request):
    return render(request,'earn/spinning.html')    

@login_required
def patt(request):
  if request.method == 'POST' :
    pat_form = Pat()
 
    if pat_form.is_valid():
            pat_form.save()
            messages.success(request, f'Failed! Please try Again')
            return redirect('earn-home')

    else:
        pat_form = Pat(instance=request.user)

        context = {
            'pat_form' : pat_form,
        }
        return render(request, 'earn/patt.html',context)



 
        