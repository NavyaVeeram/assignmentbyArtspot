# appname/views.py
from django.shortcuts import render

def hello(request):
    return render(request,'hello.html')
