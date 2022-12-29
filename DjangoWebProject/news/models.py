from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=30, default='Базовое название статьи')
    anons = models.CharField('Анонс', max_length=250, default='Базовый заголовок')
    full_text = models.TextField('Текст статьи', default='Базовый текст статьи')
    text_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class User(models.Model):
    login = models.CharField('Имя пользователя', max_length=20, default='Anonymus')
    password = models.TextField('Пароль', max_length=40, default='******')