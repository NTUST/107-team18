from django.contrib import admin
from .models import CourseAdminstrator, CourseInformation, CourseFile

admin.site.register(CourseAdminstrator)
admin.site.register(CourseInformation)
admin.site.register(CourseFile)