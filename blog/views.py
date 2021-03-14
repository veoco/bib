from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category, Page


class PostDetail(DetailView):
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get('slug', None)
        post = Post.objects.get(slug=post_slug)
        if post.password:
            raise Http404
        return post


class PageDetail(DetailView):
    model = Page


class PostList(ListView):
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'
    paginate_by = 10
    meta = None

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug', None)
        cate_slug = self.kwargs.get('cate_slug', None)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            self.meta = tag
            return Post.objects.filter(tag=tag, status='public')
        elif cate_slug:
            cate = get_object_or_404(Category, slug=cate_slug)
            self.meta = cate
            return Post.objects.filter(category=cate, status='public')
        else:
            return Post.objects.filter(status='public')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = self.meta
        return context
