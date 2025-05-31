from django.contrib import admin
from .models import students , teachers , classes,subjects,teacher_class_subject , attendance

admin.site.register(students)
admin.site.register(teachers)
admin.site.register(classes)
admin.site.register(subjects)
admin.site.register(teacher_class_subject)
admin.site.register(attendance)
