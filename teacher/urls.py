from django.urls import path
from teacher import views

urlpatterns  = [
    path('teacher-login/', views.teacher_login, name='teacher-login'),
    path('teacher-landing/<str:owner>/', views.teacher_landing_page, name='teacher-landing'),
    path('classroom/<str:owner>/<str:title>/', views.classroom, name='classroom'),
    path('teacher_logout/', views.logout_teacher, name='teacher-logout')
]