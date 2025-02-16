from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_sense_sessio, name='login'),
    path('inici/', views.inici, name='inici'),  
    path('login-sessio/', views.login_amb_sessio, name='login_amb_sessio'),
    path('logout/', views.logout, name='logout'),
]