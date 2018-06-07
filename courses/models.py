from django.db import models
from django.contrib.auth.models import User

class CourseAdminstrator(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_name = models.CharField(max_length=20)

    def __str__(self):
        return self.admin_name

class CourseInformation(models.Model):
    course_administrator = models.ForeignKey(CourseAdminstrator, on_delete=models.CASCADE)
    # course_no = models.CharField(max_length=20) #### blank/null
    course_name = models.CharField(max_length=20)
    course_teacher = models.CharField(max_length=20)
    course_type = models.CharField(max_length=20)
    course_discription = models.CharField(max_length=500, null=True)
    course_website = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.course_name

class CourseFile(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(CourseInformation, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', default=None, on_delete=models.DO_NOTHING, null=True, blank=True)
    cfile = models.FileField(upload_to='static/files/courses/', max_length=100)
    cfile_class = models.CharField(max_length=20) # COMMENT 'Handout/Homework/Exam'
    cfile_year = models.CharField(max_length=4) # Defalut Year Now # max next year
    cfile_content = models.CharField(max_length=100)
    # cfile_subname = models.CharField(max_length=20) # 表單裡面沒有

    def __str__(self):
        return self.cfile_content