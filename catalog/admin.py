from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_version', 'name_version', 'indicates_version')
    list_filter = ('indicates_version',)
    search_fields = ('number_version', 'name_version')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
