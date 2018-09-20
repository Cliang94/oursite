from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''用户简介'''
    #用户
    user=models.OneToOneField(User,unique=True)
    #出生日期
    birth=models.DateTimeField(null=True)
    #手机号
    phone=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.user.username

class UserInfo(models.Model):
    '''用户详细信息'''
    user=models.OneToOneField(User,unique=True)
    school=models.CharField(max_length=100,blank=True)
    company=models.CharField(max_length=100,blank=True)
    profession=models.CharField(max_length=200,blank=True)
    adress=models.CharField(max_length=200,blank=True)
    description=models.TextField(blank=True)
    photo=models.ImageField(blank=True,upload_to='images')

    def __str__(self):
        return self.user.username
