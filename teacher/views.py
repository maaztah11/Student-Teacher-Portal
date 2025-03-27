from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('teacher-name')
        email = request.POST.get('teacher-email')
        authenticated_user = authenticate(request, username=username, email=email)
        if authenticated_user is not None:
            request.session['username'] = authenticated_user.username
            login(request, authenticated_user)
            next_url = request.GET.get('next', 'teacher-landing')
            messages.success(request, 'Login was successfull')
            return redirect('teacher-landing', owner=username)
        else:
            messages.error(request, 'Login wasnt successfull')
    return render(request, 'teacher/teacher_login.html')
@login_required(login_url='teacher-login')
def teacher_landing_page(request, owner):
    print(owner)
    teacher = get_object_or_404(Teacher, teacher_name=owner)
    if request.method == 'POST':
        title = request.POST.get('classroom-title')
        code = request.POST.get('classroom-code')
        if not title or not code or not owner:
            messages.error(request, 'Fields are missing')
        else:
            classroom = ClassRoom.objects.create(title=title, code=code, owner=teacher)
            messages.success(request, 'Classroom created successfully')
            return redirect('classroom', owner , title)
    elif request.method == 'GET':
        classroom = ClassRoom.objects.filter(owner=teacher)
        context = {'classroom': classroom}
    return render(request, 'teacher/teacher-landing.html', context)
@login_required(login_url='teacher-login')
def classroom(request, owner, title):
    print(owner)
    classroom  = ClassRoom.objects.get(title = title)
    students = classroom.students.all()
    context = {'students': students}
    if request.method == 'POST':
        assignment_title = request.POST.get('title')
        file = request.FILES.get('file')
        teacher = Teacher.objects.get(teacher_name = owner)
        print(teacher, classroom)
        new_assignment = Assignment.objects.create(title=assignment_title, file=file, created_by=teacher)
        new_assignment.uploaded_to.set([classroom])
        messages.success(request, 'Assignment uploaded successfully')
        return HttpResponse('Done')

    return render(request, 'teacher/classroom.html', context)
def logout_teacher(request):
    logout(request)
    return redirect('teacher-login')
