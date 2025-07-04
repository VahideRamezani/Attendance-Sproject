from datetime import datetime, date, timedelta
from django.db.models import Q
from django.shortcuts import render, redirect
from apps.login.models import attendance, students, teachers, subjects, teacher_class_subject
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

    selected_teacher = request.GET.get('teacher_id')
    selected_subject = request.GET.get('subject_id')
    selected_date = request.GET.get('date')

    class_id = student.class_id
    tcs = teacher_class_subject.objects.filter(class_id=class_id)

    subjects_list = list(subjects.objects.filter(subject_id__in=tcs.values_list('subject_id', flat=True).distinct()))
    # teachers_list = list(teachers.objects.filter(teacher_id__in=tcs.values_list('teacher_id', flat=True).distinct()))

    # تاریخ‌ها
    date_range = []
    today = date.today()
    start_date = date(2025, 3, 20)
    current_date = start_date
    while current_date <= today:
        date_range.append({
            'gregorian': current_date.strftime('%Y-%m-%d'),
            'jalali': jdatetime.date.fromgregorian(date=current_date).strftime('%Y/%m/%d')
        })
        current_date += timedelta(days=1)
    date_range.reverse()


    absences = attendance.objects.filter(student_id=student, status='a')

    # if selected_teacher:
    #     try:
    #         absences = absences.filter(teacher_id=int(selected_teacher))
    #     except ValueError:
    #         pass

    if selected_subject:
        try:
            absences = absences.filter(subject_id=selected_subject)
        except (ValueError, TypeError):
            pass

    if selected_date:
        try:
            gdate = datetime.strptime(selected_date, '%Y-%m-%d').date()
            absences = absences.filter(date=gdate)
        except ValueError:
            pass

    if request.method == "POST":
        for key, uploaded_file in request.FILES.items():
            if key.startswith("proof_"):
                parts = key.split("_")
                if len(parts) == 2 and parts[1].isdigit():
                    attendance_id = int(parts[1])
                    try:
                        absence = attendance.objects.get(attendance_id=attendance_id, student_id=student)
                        absence.proof_image = uploaded_file
                        absence.save()
                    except attendance.DoesNotExist:
                        pass

    def get_jalali_date(gdate):
        if isinstance(gdate, (datetime, date)):
            jdate = jdatetime.date.fromgregorian(date=gdate)
            return jdate.strftime('%Y/%m/%d'), jdate.strftime('%A')
        return '', ''

    absences_with_jalali = []
    for a in absences.order_by('-date'):
        jalali_date, weekday = get_jalali_date(a.date)
        absences_with_jalali.append({
            'attendance_id': a.attendance_id,
            'proof_image': a.proof_image,
            'proof_verified': a.proof_verified,
            'subject_name': a.subject_id.subject_name if a.subject_id else '',
            'jalali_date': jalali_date,
            'weekday': weekday,
        })
    no_records = len(absences_with_jalali) == 0


    return render(request, 'panel/student.html', {
        'absences': absences_with_jalali,
        'subjects_list': subjects_list,
        # 'teachers_list': teachers_list,
        'date_range': date_range,
        # 'upload_message': upload_message,
        'first_name': student.student_name,
        'last_name': student.student_lname,
        'selected_teacher': selected_teacher,
        'selected_subject': selected_subject,
        'selected_date': selected_date,
        'no_records': no_records,
    })


def logout(request):
    request.session.flush()
    return render(request, 'home/index.html', {'messages': ['شما با موفقیت خارج شدید.']})
