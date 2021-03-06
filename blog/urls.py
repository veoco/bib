from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('tag/<slug:tag_slug>/', views.PostList.as_view(), name='tag_post'),
    path('category/<slug:cate_slug>/', views.PostList.as_view(), name='cate_post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PageDetail.as_view(), name='page_detail'),
]