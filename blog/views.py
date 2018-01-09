# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
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
        # 分类信息获取(导航数据)
        category_list = Category.objects.all()
        # 广告数据（同学们自己完成）
        # 最新文章信息
        article_list = Article.objects.all()
        paginator = Paginator(article_list,1)
        try:
            page = int(request.GET.get('page',1))
            aritcle_list = paginator.page(page)
            print aritcle_list
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
            print aritcle_list
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())