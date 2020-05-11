from basic_app import views
from django.conf.urls import url

#Template tagging:
app_name='basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),#relative page
    url(r'^other/$', views.other, name='other'),#other page
    url(r'^index/$', views.index, name='index'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^user_login/$', views.user_login,name='user_login'),
    url(r'^user_logout/$', views.user_logout,name='user_logout'),
]
