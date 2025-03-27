from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.models import *
# Create your views here.
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('std-name')
        email = request.POST.get('std-email')
        print(username, email)
        authenticated_user = authenticate(request, username=username, email=email)
        print(authenticated_user)
        print("Done")
        if authenticated_user is not None:
            print("reached if block")
            request.session['student_name'] = authenticated_user.username
            login(request, authenticated_user)
            print("login done")
            messages.success(request, 'Login was successfull')
            return redirect('join-class')
        else:
            print("Else block reached")
            messages.error(request, 'An error occured..')
    return render(request, 'student/student_login.html')
def student_logout(request):
    logout(request)
    return redirect('student-login')
def join_classroom(request):
    if request.method == 'POST':
        code = request.POST.get('class-code')
        try:
            classroom = get_object_or_404(ClassRoom, code=code)
            if classroom is not None:
                return redirect("student-dashboard", code=code)
        except ClassRoom.DoesNotExist:
            return HttpResponse("Invalid Code was entered...")
    return render(request, 'student/join_class.html')
def student_dashboard(request, code):

    classroom = get_object_or_404(ClassRoom, code=code)
    #Fetch all uplaoded assignments
    assignments = Assignment.objects.filter(uploaded_to = classroom)
    context = {'classroom': classroom,  'assignments' : assignments}
    return render(request, 'student/student_dashboard.html', context)


