from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    html = "<h1>Hello World</h1>"
    return HttpResponse(html)

def user_view(request):
    html = "<h1>Hello User</h1>"
    return HttpResponse(html)