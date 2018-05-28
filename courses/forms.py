from django import forms
from .models import CourseInformation, CourseFile

class CourseFileForm(forms.ModelForm):
    class Meta:
        model = CourseFile
        fields = ('cfile_class', 'cfile_type', 'cfile_year', 'cfile_content', 'cfile_subname',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('course_name','')
        super(CourseFileForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ModelChoiceField(queryset=CourseInformation.objects.filter(course_name=course_name))