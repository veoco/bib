from blog.models import Category


def site_info(request):
    info = {
        'name': '游匿存储'
    }
    cate = Category.objects.all()
    return {'site_info': info, 'head_cate': cate}