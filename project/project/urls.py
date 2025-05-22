from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apps.home.urls') ),
    path('' , include('apps.login.urls') ),
    path('' , include('apps.student_panel.urls') ),
    path('' , include('apps.teacher_panel.urls') ),
]
handler404 = 'apps.home.views.custom_404_view'
