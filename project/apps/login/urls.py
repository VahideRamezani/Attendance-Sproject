from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('roles/', views.roles, name='roles'),
    path('teacher/login/', views.Tlogin, name='Tlogin'),
    path('student/login/', views.Slogin, name='Slogin'),
]
