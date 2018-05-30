from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    messages.info(request, '歡迎來到 Coper Files!')
    return render(request, 'main/index.html')

# def signup(request):
#     return render('main/signup.html')

# def login(request):
#     if request.user.is_authenticated(): 
#         return HttpResponseRedirect('/index')

#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     print(username,password)
#     user = auth.authenticate(username=username, password=password)

#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('/index/')
#     else:
#         return render_to_response('main/login.html') 

# def logout(request):
#     return render_to_response('main/logout.html')