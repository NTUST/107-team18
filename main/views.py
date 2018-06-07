from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from courses.models import CourseInformation

def index(request):
    if request.user.is_authenticated:
        messages.info(request, '%s 歡迎回來!' % request.user.first_name)
    else:
        messages.info(request, '歡迎來到 Coper Files!')
    # 精選課程 (取出檔案最多的三個課程)
    courses = CourseInformation.objects.annotate(file_count=Count('coursefile')).order_by('-file_count')[:3]
    return render(request, 'main/index.html', { 'courses': courses })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, '註冊成功!')
            return login(request)
        else:
            messages.info(request, '註冊失敗!')
            return render(request, 'main/signup.html', {'form': form})

    return render(request, 'main/signup.html')

def login(request):
    if request.user.is_authenticated: 
        messages.info(request, '你已登入!')
        return index(request)

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            messages.info(request, '登入成功!')
            return index(request)
        else:
            messages.info(request, '登入失敗!')
            return render(request, 'main/login.html') 
    return render(request, 'main/login.html')

def logout(request):
    messages.info(request, '登出成功!')
    auth.logout(request)
    return index(request)