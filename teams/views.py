from django.http import request
import datetime
from django.shortcuts import render

def spin(request):
    return render(request,'teams/team.html')
