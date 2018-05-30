from django.conf.urls import url
from . import views

urlpatterns = [
    # 
    url(r'^$', views.index, name='index'),
    # index/
    url(r'^index/$', views.index, name='index'),
    # course_list/
    url(r'^course_list/$', views.course_list, name='course_list'),
    # # signup/
    # url(r'^signup/$', views.signup, name='signup'),
    # # login/
    # url(r'^login/$', views.login, name='login'),
    # # logout/
    # url(r'^logout/$', views.logout, name='logout'),
]