from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import CourseAdminstrator, CourseInformation, CourseFile
from .forms import CourseFileForm

def courses(request): # Get Pages
    # if request.method = 'POST': # Search
    #     courses = CourseInformation.objects.filter() # Filter: Admin / Teacher / Name
    # else: # Not Search
    courses = CourseInformation.objects.all()
    # Get Top 5 By Pages
    # Get Files length Depend on Pages 
    return render(request, 'courses/index.html', {'courses': courses})

def courses_detail(request, id):
    # is authorize
    try:
        course = CourseInformation.objects.get(pk=id)
    except:
        messages.info(request, '找不到課程!')
        return render(request, 'courses/index.html')

    return render(request, 'courses/detail.html', {'course': course})

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
    return render(request, 'courses/edit.html')