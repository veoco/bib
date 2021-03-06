from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category


class PostDetail(DetailView):
    model = Post


class PostList(ListView):
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'
    meta = None

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug', None)
        cate_slug = self.kwargs.get('cate_slug', None)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            self.meta = tag
            return Post.objects.filter(tag=tag)
        elif cate_slug:
            cate = get_object_or_404(Category, slug=cate_slug)
            self.meta = cate
            return Post.objects.filter(category=cate)
        else:
            return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = self.meta
        return context
