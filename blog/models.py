from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    pass


class BlogMeta(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['-order']

    def __str__(self):
        return self.name


class BlogContent(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    order = models.IntegerField(default=0)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        related_query_name='%(class)s'
    )
    template = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    allow_comment = models.BooleanField(default=True)
    allow_ping = models.BooleanField(default=True)
    allow_feed = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-order', '-created']

    def __str__(self):
        return self.title


class Category(BlogMeta):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=255)


class Tag(BlogMeta):
    pass


class Post(BlogContent):
    category = models.ManyToManyField(Category, related_name='posts', related_query_name='post', blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts', related_query_name='post', blank=True)


class Page(BlogContent):
    pass
