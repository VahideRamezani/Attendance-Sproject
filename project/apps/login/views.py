from django.shortcuts import render, redirect
from .forms import SLoginForm
from .models import students

def roles(request):
    return render(request, 'login/roles.html')

def Tlogin(request):
    return render(request, 'login/teacher.html')

def Slogin(request):
    form = SLoginForm(request.POST or None)
    error_message = None

    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['st_code'].strip()
            password = form.cleaned_data['st_password'].strip()
            if code == password:
                try:
                    student = students.objects.get(student_id=code)
                    request.session['student_id'] = student.student_id
                    return redirect('student_panel:panel')  # اینو با مسیر واقعی جایگزین کن
                except students.DoesNotExist:
                    error_message = 'دانش‌آموزی با این کد ملی یافت نشد.'
            else:
                error_message = 'کد ملی و رمز عبور باید یکسان باشند.'

    return render(request, 'login/student.html', {'form': form, 'error_message': error_message})