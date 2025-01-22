from django.urls import path
from . import views

urlpatterns = [
    
    path('centre/teachers', views.teachers, name='teachers'),
]
