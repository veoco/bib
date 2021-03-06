from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post


class PostDetail(DetailView):
    model = Post
