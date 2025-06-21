from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_data_admin')
    fieldsets = UserAdmin.fieldsets + (
        ('Permisos especiales', {
            'fields': ('is_data_admin',),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)