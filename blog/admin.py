from django.contrib import admin
from .models import Post


# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date', 'published_date')
    search_fields = ('author__username', 'title')


admin.site.register(Post, postAdmin)
