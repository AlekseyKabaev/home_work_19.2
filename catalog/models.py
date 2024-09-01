from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True, blank=True)
    image = models.ImageField(upload_to="catalog/image", verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    price = models.IntegerField(verbose_name='Стоимость продукта')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', null=True, blank=True)
    number_version = models.IntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=100, verbose_name='Название версии')
    indicates_version = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    class Meta:
        verbose_name = "Вкрсия"
        verbose_name_plural = "Версии"
        ordering = ("id",)

    def __str__(self):
        return self.name_version
