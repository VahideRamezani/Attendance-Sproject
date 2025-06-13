from django.urls import path
from . import views

app_name = 'teacher_panel'
urlpatterns = [
     path('panel/', views.panel, name='panel'),
     path('logout/', views.logout, name='logout'),
     path('update_attendance/', views.update_attendance, name='update_attendance'),

]