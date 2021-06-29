from . import models
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms.user_form import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['get_full_name', 'email', 'is_active', 'date_joined']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important Dates', {'fields': ('date_joined', 'last_login')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')}
         ),
    )

    search_fields = ('email', 'first_name', 'middle_name', 'last_name')
    ordering = ['first_name', 'middle_name', 'last_name', 'email']
    #filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)


admin.site.register([
])
