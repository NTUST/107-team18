from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
def courses(request):
    return HttpResponse('courses')

def courses_detail(request):
    return HttpResponse('detail')

def courses_files_upload(request):
    return HttpResponse('upload')

def courses_files_edit(request):
    return HttpResponse('edit')