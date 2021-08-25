from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    name = models.CharField(max_length=30)
    articles = models.ManyToManyField(Article, through='Tabel', related_name='tags')
    def __str__(self):
        return self.name
2

class Tabel(models.Model):
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE,verbose_name='Раздел')
    is_main = models.BooleanField(default=False,verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')

    class Meta:
        verbose_name = 'раздел для статьи'
        verbose_name_plural = 'Тематика статьи'