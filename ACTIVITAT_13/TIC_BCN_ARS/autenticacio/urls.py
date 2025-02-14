from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_sense_sessio, name='login'),
    path('inici/', views.inici, name='inici'),  
]