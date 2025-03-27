from django.urls import path
from student import views
urlpatterns = [
    path('student-login/', views.student_login, name='student-login' ),
    path('student-logout', views.student_logout, name='student-logout'),
    path('join_class/', views.join_classroom, name='join-class'),
    path('student_dashboard/<str:code>/', views.student_dashboard, name='student-dashboard')
]