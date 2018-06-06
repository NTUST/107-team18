from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import MyUser

# def users_panel(request):
# 	# is authorize
#     return render(request, 'users/index.html') 

# def users_profile(request):
# 	# is authorize
#     return render(request, 'users/profile.html') 

# def users_files(request):
# 	# is authorize
#     return render(request, 'users/files.html') 

def users_panel(request):
	# is authorize
    return render(request, 'users/files.html')