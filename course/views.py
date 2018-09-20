from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from course.models import Course,Lession
from django.views import View
from django.shortcuts import get_list_or_404
from braces.views import LoginRequiredMixin

#序列化
from rest_framework import generics
from course.serializers import CourseSerializers
class Cate(generics.ListCreateAPIView):
    queryset =Course.objects.all()
    serializer_class = CourseSerializers


class Cam(generics.RetrieveUpdateDestroyAPIView):
    queryset =Course.objects.all()
    serializer_class = CourseSerializers


# Create your views here.

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course_List.html'
class LessionsListView(TemplateView,View):
    template_name = 'course/lesson_list.html'
    def get(self, request,course_id):
        course=get_list_or_404(Course,id=course_id)
        return self.render_to_response({'courses':course})



 #管理员创建 Course,需要登陆验证
class UserMixin:
    #Mixin:混合
    #这个类要和别的类混合在一起使用，在命名类的时候在末尾加上Mixin
    def get_querusets(self):
        querysets=super(UserMixin,self).get_queryset()
        return querysets.filter(user=self.request.user)

class UserCourseMixin(UserMixin,LoginRequiredMixin):
    # 设定当前类从哪个模型读取数据
    model = Course
    # 设定如果没有登录,重定向的登录地址是什么
    login_url = '/account/login/'


class ManageCourseListView(UserCourseMixin, ListView):
    """通过UserCourseMixin类为当前类添加登录限制,即只有登录才能访问当前类视图"""
    context_object_name = 'courses'
    template_name = 'course/manage/course_list.html'

