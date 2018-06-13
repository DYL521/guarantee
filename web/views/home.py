#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from django.http import JsonResponse
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
    else:
        article_type_id = None
        base_url = '/'

    if article_type_id == 5:  ## 返回妹子图片
        article_type_id = 5
        meizi_list = models.MeiZi.objects.all()

        return render(request,
                      'meizi.html',
                      {'article_type_id': article_type_id,
                       'article_type_list': article_type_list})
    else:
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


def get_imgs(request):
    print('------------------')
    nid = request.GET.get('nid')
    print(nid)
    # img_list = models.Img.objects.values('id','src','title') ## queryset 里面是字典
    ## 取id大于nid的
    img_list = models.MeiZi.objects.filter(nid__gt=2).values('nid', 'src', 'title')  ## queryset 里面是字典
    img_list = list(img_list)
    ret = {
        'status': True,
        'data': img_list
    }
    # return HttpResponse(json.dumps(ret)) ## 方式1
    return JsonResponse(ret)  ## 方式2 ： 内部json.dumps
