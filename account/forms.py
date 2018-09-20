from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile,UserInfo

class UserProfileForm(forms.ModelForm):
    '''基于Model创建form'''
    class Meta:
        #指定基于哪个Model
        model=UserProfile
        fields=("phone","birth")
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('user','school','company','adress','description','photo','profession')

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email',)

class RegisterForm(forms.ModelForm):
    #widget 对应   input中的type
    password1=forms.CharField(label='密码',widget=forms.PasswordInput)
    password2=forms.CharField(label='确认密码',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','email')
