from django import forms
from django.contrib.auth.models import User

from courses.models import CourseFile, CourseInformation


class CourseFilesForm(forms.ModelForm):
    class Meta:
        model = CourseFile
        fields = ("cfile", "cfile_class", "cfile_year", "cfile_content")
        exlcude = ("uploader", "course", "cfile")

    def __init__(self, *args, **kwargs):
        super(CourseFilesForm, self).__init__(*args, **kwargs)
