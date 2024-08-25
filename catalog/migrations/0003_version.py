# Generated by Django 5.0.7 on 2024-08-25 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(verbose_name='Номер версии')),
                ('name_version', models.CharField(max_length=100, verbose_name='Название версии')),
                ('indicates_version', models.BooleanField(default=False, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Вкрсия',
                'verbose_name_plural': 'Версии',
                'ordering': ('id',),
            },
        ),
    ]
