import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger('blog.views')

# Create your views here.
def global_settings(request):
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
        file = open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())