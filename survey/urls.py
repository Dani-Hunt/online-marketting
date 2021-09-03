from . import views
from django.urls import path

urlpatterns = [

    path('pattern/',views.pattern, name = 'pattern'),
    path('surv/', views.survey, name = 'surv')
]