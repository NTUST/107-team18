from django.conf.urls import url
from . import views

urlpatterns = [
    # courses/
    url(r'^$', views.courses, name='courses'),
    # courses/<course_no>  # couser_no 為 XX123214124
    url(r'^(?P<id>[\d]+)/$', views.courses_detail, name='courses_detail'),
    # courses/upload
    url(r'^upload/$', views.courses_files_upload, name='courses_files_upload'),
    # courses/edit
    url(r'^edit/$', views.courses_files_edit, name='courses_files_edit'),
]