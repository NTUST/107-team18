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

def courses_detail(request, course_no):
    # is authorize
    try:
        course = CourseInformation.objects.get(course_no=course_no)
    except:
        messages.info(request, '�Ҳ����n��!')
        raise render(request, 'courses/index.html')

    return render(request, 'courses/detail.html', {'course': course})

def courses_files_upload(request): # ���� files �M��
    # is authorize
    if request.Post: #������ς��n��
        form = CourseFileForm(request.POST)
        if form.is_valid():
            courses = form.save()
    # ��t�³� �ς��n�������

    return HttpResponse('upload')

def courses_files_edit(request):
    # is authorize
    return HttpResponse('edit')