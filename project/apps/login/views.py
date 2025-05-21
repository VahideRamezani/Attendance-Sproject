from django.shortcuts import render

def roles(request):
    return render(request, 'login/roles.html')

def Tlogin(request):
    return render(request, 'login/teacher.html')

def Slogin(request):
    return render(request, 'login/student.html')