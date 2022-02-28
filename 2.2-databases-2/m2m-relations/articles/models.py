from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Chapter(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название тематики')
    news = models.ManyToManyField(
        Article, verbose_name='Название новости', blank=True, through='ArticleChapter')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.name


class ArticleChapter(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name='Название новости', related_name='scopes')
    tag = models.ForeignKey(Chapter, on_delete=models.CASCADE,
                            verbose_name='Название тематики', related_name='scopes')
    main = models.BooleanField(verbose_name='Основной', default=False)
