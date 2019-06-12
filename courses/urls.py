from django.urls import path

from courses.views import courses, courses_detail, courses_edit, courses_files_upload

urlpatterns = [
    path("", courses, name="courses"),
    path("<int:id>", courses_detail, name="courses_detail"),
    path("edit", courses_edit, name="courses_edit"),
    path("upload/<int:id>/", courses_files_upload, name="courses_files_upload"),
]
