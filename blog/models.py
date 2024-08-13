from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=100, verbose_name='Заголовок блога')
    slug = models.CharField(max_length=100, verbose_name='заголовок', null=True, blank=True)
    content = models.TextField(verbose_name='Содержимое блога', null=True, blank=True)
    image = models.ImageField(upload_to="catalog/image", verbose_name='Изображение', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    sign_of_publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_counter = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
