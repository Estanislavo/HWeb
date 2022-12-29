# Generated by Django 4.1.4 on 2022-12-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Базовое название статьи', max_length=30, verbose_name='Название')),
                ('anons', models.CharField(default='Базовый заголовок', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(default='Базовый текст статьи', verbose_name='Текст статьи')),
                ('text_date', models.DateTimeField(default='1 января 2023', verbose_name='Дата публикации')),
            ],
        ),
    ]