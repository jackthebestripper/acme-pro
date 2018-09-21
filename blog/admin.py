from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

admin.site.register(Post, PostModelAdmin)
