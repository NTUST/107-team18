from django.conf.urls import url
from . import views

urlpatterns = [
    # 
    url(r'^$', views.index, name='index'),
    # index/
    url(r'^index/$', views.index, name='index'),
    # # signup/
    # url(r'^signup/$', views.signup, name='signup'),
    # # login/
    # url(r'^login/$', views.login, name='login'),
    # # logout/
    # url(r'^logout/$', views.logout, name='logout'),
]