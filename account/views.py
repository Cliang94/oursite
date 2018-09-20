
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# from account.models import UserProfile, UserInfo
from account.forms import RegisterForm
from account.forms import UserProfileForm

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 登录验证
        user = authenticate(username=username,password=password)
        # 如果验证通过,把user保存到request请求会话中
        if user:
            login(request,user)
            return HttpResponse('登录成功!')
        else:
            return HttpResponse('登录失败!')

    if request.method == 'GET':
        # 返回登录页面
        return render(request,'account/login.html')

def register(request):


    # if request.method == 'POST':
    #     data = request.POST
    #     username = data.get('username')
    #     password1 = data.get('password1')
    #     password2 = data.get('password2')
    #     birth  = data.get('birth')
    #     phone = data.get('phone')
    #     email = data.get('email')

    # 使用form完成注册
    if request.method == 'POST':

        user_form = RegisterForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        new_user = user_form.save(commit=False)
        # 从user_form中提取password1
        new_user.set_password(user_form.cleaned_data['password1'])
        # 保存user
        new_user.save()

        new_user_profile = user_profile_form.save(commit=False)
        # 关联user_profile 和  user
        new_user_profile.user = new_user
        # 保存user_profile
        new_user_profile.save()
        from account.models import UserInfo
        UserInfo.objects.create(user=new_user)
        return redirect(reverse("account:user_login"))



    if request.method == 'GET':
        # 把注册表单发送给用户
        return render(request,'account/register.html')















