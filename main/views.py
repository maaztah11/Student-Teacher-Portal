from django.shortcuts import render , redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    users = User.objects.all()
    context = {
        'student_count': student_count,
        'teacher_count': teacher_count,
        'users': users
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        print(username, email, role)

        try:
            if role == 'Student':
                    user = User.objects.create(username=username, email=email)
                    student_group, created = Group.objects.get_or_create(name='Student')
                    user.groups.add(student_group)
                    Student.objects.create(name=username, user=user)
                    messages.success(request, 'Student profile created successfully.')
            elif role == 'Teacher':
                    user = User.objects.create(username=username, email=email)
                    teacher_group, created = Group.objects.get_or_create(name='Teacher')
                    user.groups.add(teacher_group)
                    Teacher.objects.create(teacher_name=username, user=user)
                    messages.success(request, 'Teacher profile created successfully.')
            else:
                    messages.error(request, 'Invalid role selected.')
        except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'main/admin.html', context)
def delete(request, id):
      user = User.objects.get(id=id)
      if user:
         user.delete()
         messages.error(request, 'Student deleted successfully')
         return redirect('index')
      else:
            messages.error(request, 'No matching Student found')
def edit(request, id):
      if request.method == 'GET':
            return render(request, 'main/edit.html')
      elif request.method == 'POST':
            user = User.objects.get(id=id)
            username = request.POST.get('username', user.username)
            email = request.POST.get('email', user.email)
            user.username = username
            user.email = email
            user.save()
            return redirect('index')

                  

            
             


      