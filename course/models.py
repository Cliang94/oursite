from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Course(models.Model):
    '''python  全栈开发'''
    #课程所有者
    user=models.ForeignKey(User,related_name='course_user')
    #课程名
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    student=models.ManyToManyField(User,related_name='joined_course')
    def __str__(self):
        return self.title

class Lession(models.Model):
    user=models.ForeignKey(User,related_name='lession_user')
    title=models.CharField(max_length=150)
    course=models.ForeignKey(Course,related_name='lession_course')
    video=models.FileField(upload_to='videos')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

