from django.conf.urls import url
from . import views

urlpatterns = [
    # users
    url(r'^$', views.users_panel, name='users_panel'),
    # users/profile
    url(r'^profile/$', views.users_profile, name='users_profile'),
    # users/files
    url(r'^files/$', views.users_files, name='users_files'),
]