from datetime import datetime, date

from django.shortcuts import render, redirect
from apps.login.models import attendance, students
import jdatetime
from django.contrib import messages
from datetime import datetime, date

def panel(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login:Slogin')

    try:
        student = students.objects.get(student_id=student_id)
    except students.DoesNotExist:
        return redirect('login:Slogin')

    upload_message = ""
    if request.method == "POST":
        absences = attendance.objects.filter(student_id=student, status='a')
        for absence in absences:
            file_key = f'proof_{absence.attendance_id}'
            if file_key in request.FILES:
                absence.proof_image = request.FILES[file_key]
                absence.save()
                upload_message = f"عکس غیبت دانش‌آموز {student.student_name} {student.student_lname} ثبت شد!"

    absences = attendance.objects.filter(student_id=student, status='a').order_by('-date')

    def get_jalali_date(gdate):
        if isinstance(gdate, (datetime, date)):
            jdate = jdatetime.datetime.fromgregorian(datetime=gdate)
            return jdate.strftime('%Y/%m/%d'), jdate.strftime('%A')
        else:
            try:
                dt = datetime.strptime(str(gdate), '%Y-%m-%d')
                jdate = jdatetime.datetime.fromgregorian(datetime=dt)
                return jdate.strftime('%Y/%m/%d'), jdate.strftime('%A')
            except:
                return '', ''

    absences_with_jalali = []
    for a in absences:
        jalali_date, weekday = get_jalali_date(a.date)
        a.subject_name = a.subject_id.subject_name if a.subject_id else 'نامشخص'
        proof_verified = a.proof_verified
        absences_with_jalali.append({
            'absence': a,
            'jalali_date': jalali_date,
            'weekday': weekday,
            'proof_verified': proof_verified,
        })

    for a in absences:
        a.jalali_date, a.weekday = get_jalali_date(a.date)

    return render(request, 'panel/student.html', {
        'absences': absences,
        'upload_messages': upload_message,
    })

def logout(request):
    request.session.flush()
    return render(request, 'home/index.html', {'messages': ['شما با موفقیت خارج شدید.']})

