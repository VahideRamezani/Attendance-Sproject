from django.db import models
from django.contrib.auth.models import User


class classes(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return  str(self.class_id)

class students(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    student_name = models.CharField(max_length=100)
    student_lname = models.CharField(max_length=100)
    class_id = models.ForeignKey(classes , on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

class teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    teacher_lname = models.CharField(max_length=100)
    def __str__(self):
        return self.teacher_name

class subjects(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    def __str__(self):
        return self.subject_name

class teacher_class_subject(models.Model):
    teacher_class_subject_id = models.IntegerField(primary_key=True)
    teacher_id = models.ForeignKey(teachers, on_delete=models.CASCADE)
    class_id = models.ForeignKey(classes, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjects , on_delete=models.CASCADE)
    def __str__(self):
        return str(self.teacher_class_subject_id)

class attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students , on_delete=models.CASCADE)
    class_id = models.ForeignKey(classes , on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjects , on_delete=models.CASCADE, null=True, blank=True)  # میتونی به دلخواه پر یا خالی باشه
    teacher_id = models.ForeignKey(teachers , on_delete=models.CASCADE)
    date = models.DateField()  # تغییر داده شده به DateField
    status_choice = (
        ('a', 'absent'),
        ('p', 'present'),
        ('l', 'late')
    )
    status = models.CharField(max_length=1, choices=status_choice)
    proof_image = models.ImageField(upload_to='attendance/images/', null=True, blank=True)
    proof_verified = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.get_status_display()
