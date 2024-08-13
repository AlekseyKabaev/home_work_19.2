from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content', 'created_at')
#     # list_filter = ('category',)
#     # search_fields = ('name', 'description')

