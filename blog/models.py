from django.db import models
from users.models import User


class Article(models.Model):
    """Модель статьи, которая может быть публичной или закрытой."""
    title = models.CharField(max_length=200, verbose_name='название')
    content = models.TextField(verbose_name='содержание')
    is_public = models.BooleanField(default=True, verbose_name='публичная')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменена')

    def __str__(self):
        return f'Статья: {self.title}(автор: {self.author})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
