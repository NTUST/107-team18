from django.contrib import admin

from courses.models import CourseFile, CourseAdminstrator, CourseInformation

admin.site.register(CourseAdminstrator)
admin.site.register(CourseInformation)
admin.site.register(CourseFile)
