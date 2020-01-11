from django.contrib import admin

# Register your models here.

from .models import Post, Fernando, Category

admin.site.register(Post)
admin.site.register(Fernando)
admin.site.register(Category)
