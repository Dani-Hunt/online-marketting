from django.urls import path
from . import views

urlpatterns = [
    path('dash/',views.home, name = 'earn-home'),
    path('withdraw/',views.withdraw, name = 'withdraw'),



]