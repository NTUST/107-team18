from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    # courses/
    url(r'^$', views.courses, name='courses'),
    # courses/<course_no>  # couser_no 為 XX123214124
    url(r'^(?P<id>[\d]+)/$', views.courses_detail, name='courses_detail'),
=======
>>>>>>> e8353929ef9e037fc5d3d8c5e745a1a2c62e24f8
    # courses/upload
    url(r'^upload/$', views.courses_files_upload, name='courses_files_upload'),
    # courses/edit
    url(r'^edit/$', views.courses_files_edit, name='courses_files_edit'),
    # courses/
    url(r'^$', views.courses, name='courses'),
    # courses/<course_no>  # couser_no 為 XX123214124
    url(r'^(?P<course_no>[\w]+)/$', views.courses_detail, name='courses_detail'),
]