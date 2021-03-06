from django.urls import path

from . import views


urlpatterns = [
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]