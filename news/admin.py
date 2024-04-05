from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ('type', 'time_in', 'author', 'rating')
    list_filter = ('rating', 'time_in', 'author')

class CategoryAdmin(TranslationAdmin):
    model = Category

class PostTranslarion(PostAdmin, TranslationAdmin):
    model = Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)