from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    # path('404/', views.ss404, name='ss404'),
]