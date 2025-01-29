from django.urls import path
from . import views

urlpatterns = [

    path('teachers/', views.profes, name='teachers'),
    path('students/', views.students, name='students'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
]
