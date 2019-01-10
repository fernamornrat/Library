from django.contrib import admin
from .models import Category, Book

# Register your models here.
admin.site.register(Category)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_code', 'book_title', 'author_name', 'publisher', 'category',)
    search_fields = ('book_code', 'book_title',)
admin.site.register(Book, BookAdmin)