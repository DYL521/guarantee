#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from .base import BaseForm
from django import forms as django_forms


class RegisterForm(BaseForm, django_forms.Form):
    username = django_forms.CharField(
        max_length=12,
        required=True,
    )
    password = django_forms.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\%\^\&\*\(\)])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}$',
        min_length=8,
        max_length=32,
        error_messages={
            'required': '密码不能为空',
            'invalid': '密码必须包含数字，字母，特殊字符',
            'min_length': '密码长度不能小于8个字符',
            'max_length': '密码长度不能大于32个字符'
        }
    )
    confirm_wd = django_forms.CharField(required=True)

    ## 单个验证完成后，最后执行这个clean方法
    ## 这里才能拿到完整的数据
    def clean(self):
        v1 = self.cleaned_data['password']
        v2 = self.cleaned_data['confirm_pwd']
        if v1 == v2:
            pass
        else:
            from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
            raise ValidationError('两次密码不一致')
