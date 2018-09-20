from django.contrib import admin

# Register your models here.
from course.models import Course,Lession

admin.site.register(Course)
admin.site.register(Lession)
