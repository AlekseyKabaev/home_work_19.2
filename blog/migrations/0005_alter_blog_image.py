# Generated by Django 5.0.7 on 2024-08-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/image', verbose_name='Изображение'),
        ),
    ]
