from django.urls import path
from . import views

app_name = 'teacher_panel'
urlpatterns = [
     path('teacher/panel/', views.panel, name='panel'),
]