#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from django.http import HttpResponse
from django.shortcuts import render
from ..forms import account


def register(request):
    if request.method == 'GET':
        print(request.GET)
        form = account.RegisterForm(request)
        return render(request, 'register.html', {"form": form})
    elif request.method == 'POST':
        print('-----------A')
        print(request.POST)
        form = account.RegisterForm(request.POST)
        if form.is_valid():
            print('-----------B')
            print(form.cleaned_data)

        return render(request, 'register.html')
