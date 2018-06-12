#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from django.shortcuts import render, HttpResponse
from repository import models
from django.urls import reverse
from utils.pagination import Pagination


def index(request, *args, **kwargs):
    '''
    博客首页，展示全部博文
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    article_type_list = models.Article.type_choices

    if kwargs:
        article_type_id = int(kwargs['article_type_id'])
        base_url = reverse('index', kwargs=kwargs)
        print(base_url)
        print(article_type_id)

    else:
        article_type_id = None
        base_url = '/'

    print('-------------',request.GET)
    # ## 得到全部的数据
    data_count = article_list = models.Article.objects.filter(**kwargs).count()

    ## 分页对象
    page_obj = Pagination(1, data_count=data_count)
    article_list = models.Article.objects.filter(**kwargs).order_by(('-nid'))[page_obj.start:page_obj.end]
    page_str = page_obj.page_str(base_url=base_url)

    return render(
        request,
        'index.html',
        {
            'article_list': article_list,
            'article_type_id': article_type_id,
            'article_type_list': article_type_list,
            'page_str': page_str,
        }
    )
