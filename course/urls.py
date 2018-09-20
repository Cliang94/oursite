from django.conf.urls import url
from course.views import CourseListView,LessionsListView,ManageCourseListView
from rest_framework import generics
from course.views import Cate,Cam
urlpatterns=[
    url(r'^list/',CourseListView.as_view(),name="course_list"),
    url(r'^(?P<course_id>[0-9]+)/',LessionsListView.as_view(),name='course_detail'),
    url(r'^cate/',Cate.as_view()),
    #管理课程表
    url(r'^manage/',ManageCourseListView.as_view(),name='manage_course')

]