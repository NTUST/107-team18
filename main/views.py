from django.contrib import auth
from django.shortcuts import render
from django.contrib import messages

def index(request):
    messages.info(request, '歡迎來到 Coper Files!')
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, '註冊成功!')
            return render(request, 'main/login.html')
    
    return render(request, 'main/signup.html')

def login(request):
    if request.user.is_authenticated(): 
        messages.info(request, '你已登入!')
        return render(request, 'main/index.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        messages.info(request, '登入成功!')
        return render(request, 'main/index.html')
    else:
        messages.info(request, '登入失敗!')
        return render(request, 'main/login.html') 

def logout(request):
    auth.logout(request)
    messages.info(request, '登出成功!')
    return render(request, 'main/index.html')