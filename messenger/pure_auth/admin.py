from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()



# Register your models here.

# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")


# admin.site.register(User, UserAdmin)
