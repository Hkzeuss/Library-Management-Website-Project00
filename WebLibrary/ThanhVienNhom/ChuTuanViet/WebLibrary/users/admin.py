from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'student_id')
    search_fields = ['first_name', 'last_name', 'email', 'student_id']

admin.site.register(User, UserAdmin)
