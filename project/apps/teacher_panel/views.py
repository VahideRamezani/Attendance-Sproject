import json
from datetime import date, timedelta, datetime

import jdatetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date

from apps.login.models import classes, students, teachers, subjects, teacher_class_subject, attendance
from .forms import TeacherFilterForm


def panel(request):
    # احراز هویت
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login_page')

    teacher = teachers.objects.get(teacher_id=teacher_id)

    # آماده کردن فیلترها
    tcs_qs = teacher_class_subject.objects.filter(teacher_id=teacher)
    classes_for_teacher = classes.objects.filter(
        class_id__in=tcs_qs.values_list('class_id', flat=True).distinct())
    subjects_for_teacher = subjects.objects.filter(
        subject_id__in=tcs_qs.values_list('subject_id', flat=True).distinct())


    selected_class = request.GET.get('class_id', '')
    selected_subject = request.GET.get('subject_id', '')
    selected_date = request.GET.get('date', None)
    selected_date_jalali_str = ''

    is_today = False
    if selected_date:
        try:
            dt = datetime.strptime(selected_date, '%Y-%m-%d').date()
            selected_date_jalali_str = jdatetime.date.fromgregorian(date=dt).strftime('%Y/%m/%d')
            if dt == date.today():
                is_today = True
        except:
            selected_date_jalali_str = selected_date  # اگر تبدیل نشد رشته اولیه بمونه
    else:
        is_today = True

    students_list = []
    if selected_class:
        students_list = students.objects.filter(class_id=selected_class)


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
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("status-"):
                student_id = key.split("-")[1]
                status = value
                # اینجا کد ذخیره وضعیت غیبت تو دیتابیس میره
                print(f"Student {student_id} has status {status}")
            elif key.startswith("confirm-"):
                student_id = key.split("-")[1]
                confirm = value
                # اینجا کد تایید/رد گواهی میره
                print(f"Student {student_id} confirm status: {confirm}")

        # بعد از ذخیره، برگرد به صفحه پنل
        return redirect('teacher_panel:panel')
    else:
        # اگر با GET اومدن، شاید برگردیم به پنل یا صفحه خطا
        return redirect('teacher_panel:panel')