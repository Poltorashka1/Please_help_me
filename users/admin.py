from django.contrib import admin
from users import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    """Расширяем стандартный Admin пользователя"""
    list_display = ('username', 'email',)
    ordering = ('-username',)

    # def get_fieldsets(self, request, obj=None):
    #     fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
    #     new_fieldsets = list(fieldsets)
    #     new_fieldsets[0] = (
    #         None,
    #         {'fields': ('username', 'email', 'phone', 'password')})
    #     return new_fieldsets
