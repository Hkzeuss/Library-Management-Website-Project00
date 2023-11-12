from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'first_name', 'last_name', 'desc']

admin.site.register(Profile, ProfileAdmin)
