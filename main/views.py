from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html')

def signup(request):
    return render_to_response('main/signup.html')

def login(request):
    return render_to_response('main/login.html')

def logout(request):
    return render_to_response('main/logout.html')