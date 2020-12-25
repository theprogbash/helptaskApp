from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from account_app.models import CustomUser

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (_('Ümumi məlumatlar'), {'fields': ('username', 'password', 'email', 'first_name', 'last_name',  'user_image', 'phone_number')}),
        (_('İstifadəçi hesabı'), {'fields': ('date_joined', 'last_login')}),
        (_('Hüquqlar'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (
            _('Ümumi məlumatlar'),
            {
                'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'user_image', 'is_active')
            }
        ),
    )

    list_display = ('username', 'phone_number',)

    search_fields = ('username',)
    
    ordering = ('date_joined',)

admin.site.register(CustomUser, UserAdmin)
