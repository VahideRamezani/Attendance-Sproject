from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apps.home.urls') ),
    path('' , include('apps.login.urls') ),
    path('' , include('apps.student_panel.urls') ),
    path('' , include('apps.teacher_panel.urls') ),
    path('captcha/', include('captcha.urls')),
]
handler404 = 'apps.home.views.custom_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
