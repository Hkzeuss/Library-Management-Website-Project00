from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author__title', 'translater', 'publisher', 'category__title', 'student__username']

admin.site.register(Book, BookAdmin)
