from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class ClassRoom(models.Model):
    title = models.CharField(max_length=40)
    code = models.CharField(max_length=10)
    owner = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classroom', null=True, blank=True)
class Submission(models.Model):  
    submission_date = models.DateField(null=True, blank=True)  
    student = models.ForeignKey('Student', on_delete=models.CASCADE)  
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)  
    file = models.FileField(upload_to='submissions/', null=True, blank=True) 
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.student.name} for {self.assignment.title}"

    class Meta:
        unique_together = ('student', 'assignment')  
class Assignment(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='Assignments/', null=True, blank=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    uploaded_to = models.ManyToManyField(ClassRoom, related_name='assignments')
class Announcment(models.Model):
    message = models.CharField(max_length=500)
    sent_by = models.ManyToManyField(Teacher, related_name='sender')
    room = models.ManyToManyField(ClassRoom, related_name='room')


