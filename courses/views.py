from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from .models import CourseAdminstrator, CourseInformation, CourseFile
from .forms import CourseFileForm

def courses(request):
    courses = CourseInformation.objects.all()
    return render(request, 'courses/index.html', {'courses', courses})

def courses_detail(request, course_no):
    # is authorize
    try:
        course = CourseInformation.objects.get(course_no=course_no)
    except Exception as e:
        courses = None
        raise Http404("找不到頁面")
        # Redirect to courses page

    return render(request, 'courses/detail.html', {'course', course})

def courses_files_upload(request): # 帶著 files 進來
    # is authorize
    if request.Post: #如果是上傳檔案
        form = CourseFileForm(request.POST)
        if form.is_valid():
            courses = form.save()
    # 否則吐出 上傳檔案的頁面

    return HttpResponse('upload')

def courses_files_edit(request):
    # is authorize
    return HttpResponse('edit')