from django.conf.urls import url
from . import views

urlpatterns = [
    # courses/
    url(r'^$', views.courses, name='courses'),
    # courses/id # courses/1
    url(r'^(?P<id>[\d]+)/$', views.courses_detail, name='courses_detail'),
    # courses/edit
    url(r'^edit/$', views.courses_edit, name='courses_edit'),

    # courses/upload/id
    url(r'^upload/(?P<id>[\d]+)/$', views.courses_files_upload, name='courses_files_upload'),
]