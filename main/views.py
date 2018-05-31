from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from courses.models import CourseFile

def index(request)
    messages.info(request, '歡迎來到 Coper Files!')
    # 精選課程 (取出檔案最多的三個課程)
    # courses = CourseFile.objects.values('id').annotate(files_count=Count('files')).order_by('-files_count')[:3]
    return render(request, 'main/index.html')

def signup(request):
    return render('main/signup.html')

def login(request):
    if request.user.is_authenticated(): 
        messages.info(request, '你已登入!')
        return render(request, 'main/index.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username,password)
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        messages.info(request, '登入成功!')
        return render(request, 'main/index.html')
    else:
        messages.info(request, '登入失敗!')
        return render(request, 'main/login.html') 

def logout(request):
    messages.info(request, '登出成功!')
    return render(request, 'main/logout.html')