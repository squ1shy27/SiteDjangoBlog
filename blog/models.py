from django.utils import timezone
from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    # Класс наследуемый, для определения статусов постов

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Заголовок поста
    title = models.CharField(max_length=250)
    # Хранение части юрл поста
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Поле для связи таблиц Post and User
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_post')
    # Содержимое статьи
    body = models.TextField()

    # дата публикации
    publish = models.DateTimeField(default=timezone.now)
    # дата созадния
    created = models.DateTimeField(auto_now_add=True)
    # Дата изменения
    update = models.DateTimeField(auto_now=True)
    # Статус статьи
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager() # менеджер, применяемый по умолчанию
    published = PublishedManager() # пользовательский менеджер
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug,
                                                 ])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
