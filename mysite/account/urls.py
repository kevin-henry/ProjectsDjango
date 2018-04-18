from django.conf.urls import url
from . import  views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^login/$',auth_views.login,name='user_login'),
    url(r"^newlogin/$",auth_views.login,{"template_name":"account/login.html"},name='user_newlogin'),
    #url(r'^logout/$',auth_views.logout,name='user_logout'),
    url(r'^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name='user_logout'),
]