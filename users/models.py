from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to="users/avatars", verbose_name='Аватар', help_text='Загрузите аватар', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', help_text='Введите номер телефона', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Введите страну проживания', null=True, blank=True)

    token = models.CharField(max_length=100, verbose_name='Token', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
