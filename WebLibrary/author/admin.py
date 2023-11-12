from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Author, AuthorAdmin)
