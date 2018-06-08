from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import CourseAdminstrator, CourseInformation, CourseFile
from .forms import CourseFileForm

def handle_uploaded_file(f):
    path = 'static/files/courses/'
    with open(path + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def courses(request):
    if request.method == 'POST': # Search
        # 屬性名稱: course_administrator__admin_name / course_teacher / course_name
        # 屬性名稱__icontains='搜尋條件'
        # contains 區分大小寫 / icontains 不區分大小寫
        mode = request.POST.get('mode')
        codintion = request.POST.get('condition')
        if mode == 'admin':
            courses = CourseInformation.objects.filter(course_administrator__admin_name__icontains=codintion).annotate(file_count=Count('coursefile')).order_by('-file_count')
        elif mode == 'teacher':
            courses = CourseInformation.objects.filter(course_teacher__icontains=codintion).annotate(file_count=Count('coursefile')).order_by('-file_count')
        elif mode == 'name':
            courses = CourseInformation.objects.filter(course_name__icontains=codintion).annotate(file_count=Count('coursefile')).order_by('-file_count')
        else:
            messages.info(request, '搜尋錯誤!')
            courses = CourseInformation.objects.annotate(file_count=Count('coursefile')).order_by('-file_count')
    else:
        courses = CourseInformation.objects.annotate(file_count=Count('coursefile')).order_by('-file_count')
        
    if courses:
        courses = courses[:10]

    return render(request, 'courses/index.html', {'courses': courses})

def courses_detail(request, id):
    if not request.user.is_authenticated:
        messages.info(request, '請先登入')
        return redirect('login')

    try:
        course = CourseInformation.objects.get(pk=id)
    except:
        messages.info(request, '找不到課程!')
        return render(request, 'courses/index.html')

    handouts = CourseFile.objects.filter(course=course, cfile_class__icontains="handout")
    homeworks = CourseFile.objects.filter(course=course, cfile_class__icontains="homework")
    exams = CourseFile.objects.filter(course=course, cfile_class__icontains="exam")

    return render(request, 'courses/detail.html', {'course': course, 'handouts':handouts, 'homeworks':homeworks, 'exams':exams})

def courses_edit(request):
    if not request.user.is_authenticated:
        messages.info(request, '請先登入!')
        return redirect('login')

    if not request.user.is_superuser:
        messages.info(request, '你必須是管理員!')
        return redirect('index')

    return render(request, 'courses/edit.html')

def courses_files_upload(request, id): # 帶著 files 進來
    if not request.user.is_authenticated:
        messages.info(request, '請先登入!')
        return redirect('login')

    try:
        course = CourseInformation.objects.get(pk=id)
    except:
        messages.info(request, '找不到課程!')
        return redirect('courses')

    if request.method == 'POST': #如果是上傳檔案
        form = CourseFileForm(request.POST, request.FILES)
        form.uploader = User.objects.get(username=request.user)
        if form.is_valid():
            cform = form.save(commit=False)
            cform.uploader = User.objects.get(username=request.user)
            cform.course = course
            cform.save()
            handle_uploaded_file(request.FILES['cfile'])

            messages.info(request, '上傳成功!')
            return redirect('courses_detail', id=id)

        messages.info(request, '上傳失敗!')
        return render(request, 'courses/upload.html', {'course': course, 'form': form})

    return render(request, 'courses/upload.html', {'course': course})