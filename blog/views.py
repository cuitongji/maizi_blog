# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from django.db import connection
from models import *

logger = logging.getLogger('blog.views')

# Create your views here.
def global_setting(request):
    return {'SITE_URL': settings.SITE_URL,
            'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,
            'WEIBO_SINA': settings.WEIBO_SINA,
            'WEIBO_TENCENT': settings.WEIBO_TENCENT,
            'PRO_RSS': settings.PRO_RSS,
            'PRO_EMAIL': settings.PRO_EMAIL,
    }

def index(request):
    try:
        # 最新文章数据
        category_list = Category.objects.all()
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
        # 文章归档
        # 1、先要去获取到文章中有的年份-月份  2015/06文章归档
        # 使用values和distinct去掉重复数据（不可行）
        archive_list = Article.objects.distinct_date()
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())

def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.objects.filter(date_publish__icontains=year+'-'+month)
        paginator = Paginator(article_list,2)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)

# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 3)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


