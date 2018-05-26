from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

def users_panel():
    return HttpResponse('users_panel')

def users_profile():
    return HttpResponse('users_profile')

def users_files():
    return HttpResponse('users_files')