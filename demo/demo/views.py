# -*- coding: utf-8 -*- 
# @Time : 2020/9/24 11:02 上午 
# @Author : heaton
# @File : views.py.py

from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello world")