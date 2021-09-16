from django.urls import path
from . import views

urlpatterns = [
    path('dash/',views.home, name = 'earn-home'),
    path('withdraw/',views.withdraw, name = 'withdraw'),
    path('quiz/', views.quiz, name = 'quiz'),
    path('quiz1/', views.quiz1, name = 'quiz1'),
    path('credit/', views.credit, name = 'credit'),
    path('spin/', views.spin, name = 'spin'),
    path('patt/', views.patt, name = 'patt'),
    path('treas/', views.treasure, name = 'treas'),



]