

# Register your models here.
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['id', 'title', 'author', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author__username']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

    #TODO PG ADMIN  поставить себя

    # на странице при переходе на отдельную страницу отобразить вывод команды df -h
    # с помощью питоновского скрипта на странице по кнопке отобразить вывод команды df -h
    # с помощью питоновского скрипта на странице по кнопке отобразить вывод команды watch df -h импортировать этот скрипт в отдельный файл views использовать os
