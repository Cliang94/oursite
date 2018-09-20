from django.conf.urls import url
from account.views import user_login,register
urlpatterns=[
    url(r'^login/',user_login,name='user_login'),
    url(r'^register/',register,name='user_register')
]
