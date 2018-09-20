from django.contrib import admin
from account.models import UserProfile

# Register your models here.

#自定义模型显示的内容
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone')
    list_filter = ('phone',)
# admin.site.register(UserProfile)
admin.site.register(UserProfile,UserProfileAdmin)
