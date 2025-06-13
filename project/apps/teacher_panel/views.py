import json
from datetime import date, timedelta, datetime
from django.utils.functional import cached_property
import jdatetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.utils.timezone import localdate

from apps.login.models import classes, students, teachers, subjects, teacher_class_subject, attendance
from .forms import TeacherFilterForm


def panel(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login_page')
    teacher = teachers.objects.get(teacher_id=teacher_id)

    tcs_qs = teacher_class_subject.objects.filter(teacher_id=teacher)

    classes_for_teacher = classes.objects.filter(
        class_id__in=tcs_qs.values_list('class_id', flat=True).distinct())

    subjects_for_teacher = subjects.objects.filter(
        subject_id__in=tcs_qs.values_list('subject_id', flat=True).distinct())

    selected_subject = request.GET.get('subject_id')
    selected_class = request.GET.get('class_id')
    selected_date = request.GET.get('date')
    selected_teacher = teacher

    students_list = []

    # بررسی صحت ترکیب کلاس و درس
    if selected_class and selected_subject:
        is_valid = teacher_class_subject.objects.filter(
            teacher_id=selected_teacher,
            class_id=selected_class,
            subject_id=selected_subject
        ).exists()

        if is_valid:
            students_list = students.objects.filter(class_id=selected_class)
        else:
            students_list = []  # ترکیب نامعتبره → خالی
    else:
        students_list = []

    # تاریخ انتخاب‌شده (شمسی/میلادی)
    selected_date_jalali_str = ''
    is_today = False
    if selected_date:
        try:
            dt = datetime.strptime(selected_date, '%Y-%m-%d').date()
            selected_date_jalali_str = jdatetime.date.fromgregorian(date=dt).strftime('%Y/%m/%d')
            is_today = (dt == date.today())
        except:
            dt = date.today()
            selected_date_jalali_str = selected_date
    else:
        dt = date.today()
        selected_date_jalali_str = jdatetime.date.fromgregorian(date=dt).strftime('%Y/%m/%d')
        is_today = True

    # تاریخ‌ها
    start_date = date(2025, 3, 20)
    today = date.today()
    date_range = []
    current_date = start_date
    while current_date <= today:
        date_range.append({
            'gregorian': current_date,
            'jalali': jdatetime.date.fromgregorian(date=current_date)
        })
        current_date += timedelta(days=1)
    date_range.reverse()

    # اضافه کردن عکس مدارک اگر هست
    for student in students_list:
        att = attendance.objects.filter(student_id=student, date=dt).first()
        student.proof_image_url = att.proof_image.url if att and att.proof_image else None
        student.proof_verified = att.proof_verified if att else None

    context = {
        'classes_for_teacher': classes_for_teacher,
        'subjects_for_teacher': subjects_for_teacher,
        'selected_class': selected_class,
        'selected_subject': selected_subject,
        'selected_date_jalali': selected_date_jalali_str,
        'students': students_list,
        'teacher': teacher,
        'date_range': date_range,
        'today': jdatetime.date.fromgregorian(date=today).strftime('%Y/%m/%d'),
        'is_today': is_today,
    }

    return render(request, 'panel/teacher.html', context)

def logout(request):
    request.session.flush()
    return render(request, 'home/index.html', {'messages': ['شما با موفقیت خارج شدید.']})


def update_attendance(request):
    if request.method == 'POST':
        teacher_id = request.session.get('teacher_id')
        if not teacher_id:
            return redirect('login_page')

        teacher = teachers.objects.get(teacher_id=teacher_id)
        selected_class_id = request.POST.get('class_id')
        selected_subject_id = request.POST.get('subject_id')
        selected_date_str = request.POST.get('date')

        if selected_date_str:
            try:
                selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
            except ValueError:
                selected_date = date.today()
        else:
            selected_date = date.today()

        if not (selected_class_id and selected_subject_id):
            return redirect('teacher_panel:panel')

        valid = teacher_class_subject.objects.filter(
            teacher_id=teacher,
            class_id=selected_class_id,
            subject_id=selected_subject_id
        ).exists()

        if not valid:
            return redirect('unauthorized_access')

        try:
            class_obj = classes.objects.get(class_id=selected_class_id)
            subject_obj = subjects.objects.get(subject_id=selected_subject_id)
        except (classes.DoesNotExist, subjects.DoesNotExist):
            return redirect('teacher_panel:panel')

        students_list = students.objects.filter(class_id=class_obj)

        for student in students_list:
            status = request.POST.get(f'status-{student.student_id}')
            proof_status = request.POST.get(f'proof_status-{student.student_id}')

            proof_verified = None
            if proof_status == 'approved':
                proof_verified = True
            elif proof_status == 'none':
                proof_verified = False

            if status:
                attendance.objects.update_or_create(
                    student_id=student,
                    class_id=class_obj,
                    subject_id=subject_obj,
                    teacher_id=teacher,
                    date=selected_date,
                    defaults={
                        'status': status,
                        'proof_verified': proof_verified
                    }
                )

    return redirect('teacher_panel:panel')
