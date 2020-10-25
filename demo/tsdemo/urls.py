# -*- coding: utf-8 -*- 
# @Time : 2020/10/1 3:33 下午 
# @Author : heaton
# @File : urls.py

from django.urls import path
# from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name=''),
]