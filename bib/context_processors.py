from blog.models import Category, Page


def site_info(request):
    info = {
        'name': '游匿存储'
    }
    cate = Category.objects.all()
    page = Page.objects.filter(status='public')
    return {'site_info': info, 'head_cate': cate, 'head_page': page}