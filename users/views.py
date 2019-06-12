from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from courses.models import CourseFile, CourseAdminstrator, CourseInformation
from users.models import MyUser  # not used


def users_panel(request):
    if not request.user.is_authenticated:
        messages.info(request, '請先登入')
        return render(request, 'main/login.html')

    user = User.objects.get(username=request.user)
    files = CourseFile.objects.filter(uploader=user)

    return render(request, 'users/index.html', {'files':files}) 
