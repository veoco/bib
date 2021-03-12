from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


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
    class Status(models.TextChoices):
        PUBLIC = 'public', '公开'
        PRIVATE = 'private', '私密'
        DRAFT = 'draft', '草稿'

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
    status = models.CharField(max_length=255, choices=Status.choices)
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

    def get_absolute_url(self):
        return reverse('cate_post', args=[self.slug])


class Tag(BlogMeta):
    def get_absolute_url(self):
        return reverse('tag_post', args=[self.slug])


class Post(BlogContent):
    category = models.ManyToManyField(Category, related_name='posts', related_query_name='post', blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts', related_query_name='post', blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class Page(BlogContent):
    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])
