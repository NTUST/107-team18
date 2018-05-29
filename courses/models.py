from django.db import models

class CourseAdminstrator(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_name = models.CharField(max_length=20)

    def __str__(self):
        return self.admin_name

class CourseInformation(models.Model):
    course_administrator = models.ForeignKey(CourseAdminstrator, on_delete=models.CASCADE)
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    course_teacher = models.CharField(max_length=20)
    course_type = models.CharField(max_length=20)
    course_discription = models.CharField(max_length=500, null=True)
    course_website = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.course_name

class CourseFile(models.Model):
    # uploader = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(CourseInformation, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', default=None, on_delete=models.DO_NOTHING)
    cfile_class = models.CharField(max_length=20) # COMMENT 'Handout/Homework/Exam'
    cfile_type = models.CharField(max_length=20)
    cfile_year = models.CharField(max_length=4) # Defalut Year Now # max next year
    cfile_content = models.CharField(max_length=100)
    cfile_subname = models.CharField(max_length=20)

    def __str__(self):
        return self.cfile_content

    class Meta:
        ordering = ['cfile_year', 'cfile_content']
        permissions = (
            ("can_look", "查看檔案"),
            ("can_upload", "上傳檔案"),
        )