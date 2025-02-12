from django.urls import path
from . import views

urlpatterns = [
    path('loginSense/', views.login_senseSessio, name='login_senseSessio'),
    path('inici/', views.inici, name='pagina_inici'),  
]