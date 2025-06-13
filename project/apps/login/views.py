from django.shortcuts import render, redirect
from .forms import SLoginForm , TLoginForm
from .models import students , teachers

def roles(request):
    return render(request, 'login/roles.html')

def Tlogin(request):
    form = TLoginForm(request.POST or None)
    error_message = None
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['teacher_code'].strip()
            password = form.cleaned_data['teacher_password'].strip()
            if code == password:
                try:
                    teacher = teachers.objects.get(teacher_id=code)
                    request.session['teacher_id'] = teacher.teacher_id
                    return redirect('teacher_panel:panel')
                except teachers.DoesNotExist:
                    error_message = 'معلمی با این کد پرسنلی یافت نشد.'
            else:
                error_message = 'کد ملی و رمز عبور باید یکسان باشند.'

    return render(request, 'login/teacher.html', {'form': form, 'error_message': error_message})

def Slogin(request):
    form = SLoginForm(request.POST or None)
    error_message = None

    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['st_code']
            password = form.cleaned_data['st_password']
            if code == password:
                try:
                    student = students.objects.get(student_id=code)
                    request.session['student_id'] = student.student_id
                    return redirect('student_panel:panel')
                except students.DoesNotExist:
                    error_message = 'دانش‌آموزی با این کد ملی یافت نشد.'
            else:
                error_message = 'کد ملی و رمز عبور باید یکسان باشند.'

    return render(request, 'login/student.html', {'form': form, 'error_message': error_message})