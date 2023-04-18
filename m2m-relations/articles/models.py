from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    headings = models.ManyToManyField(Heading, related_name='articles', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class TagsNews(models.Model):
    article = models.ManyToManyField(Article, related_name= ' tags')
    name = models.CharField(max_length=32, default='Разное', verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег новостей'
        verbose_name_plural = 'Теги новостей'

    def __str__(self):
        return self.name

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(TagsNews, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Тематики статьи'
        default_related_name = 'scopes'