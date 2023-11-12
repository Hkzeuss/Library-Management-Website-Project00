from django.contrib import admin
from .models import Borrow

class BorrowAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'book__title', 'borrow_date', 'return_date']

admin.site.register(Borrow, BorrowAdmin)
