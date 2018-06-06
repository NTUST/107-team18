from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import MyUser

def users_panel(request):
	# is authorize
    return render(request, 'users/index.html') 

def users_profile():
	# is authorize
    return HttpResponse('users_profile')

def users_files():
	# is authorize
    return HttpResponse('users_files')