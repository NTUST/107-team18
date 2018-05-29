from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import CourseAdminstrator, CourseInformation, CourseFile
from .forms import CourseFileForm
from django.contrib import messages

def courses(request):
    courses = CourseInformation.objects.all()
    return render(request, 'courses/index.html', {'courses', courses})

def courses_detail(request, course_no):
    if not request.user.is_authenticated():
        messages.info(request, '尚未登入!')
        return render(request, 'main/login.html')
    try:
        course = CourseInformation.objects.get(course_no=course_no)
    except Exception as e:
        messages.info(request, '找不到課程!')
        raise render(request, "courses/index.html")

    return render(request, 'courses/detail.html', {'course', course})

def courses_files_upload(request): # 帶著 files 進來
    if not request.user.is_authenticated():
        messages.info(request, '尚未登入!')
        return render(request, 'main/login.html')

    if request.Post: #如果是上傳檔案
        form = CourseFileForm(request.POST)
        if form.is_valid():
            courses = form.save()
    # 否則吐出 上傳檔案的頁面

    return render(request, 'courses/upload.html')

def courses_files_edit(request): # 先去找到原本的 Files
    if not request.user.is_authenticated():
        messages.info(request, '尚未登入!')
        return render(request, 'main/login.html')

    # 把原本的 Files 帶出去
    if request.method == 'POST':
        pass
    else: #讀取
        pass
        
    return render(request, 'courses/edit.html')