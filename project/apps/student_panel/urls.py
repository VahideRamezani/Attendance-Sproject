from django.urls import path
from . import views

app_name = 'student_panel'
urlpatterns = [
     path('student/panel/', views.panel, name='panel'),
]