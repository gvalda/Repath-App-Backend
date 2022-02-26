from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class UserAdmin(UserAdmin):
    model = User
    list_display = [
        'email',
        'username',
        'is_active',
        'is_admin',
    ]
    list_filter = (
        'is_active',
        'is_admin',
    )
    fieldsets = ((None, {'fields': ('email',
                                    'username',)}),
                 ('Avatar', {'fields': ('avatar',)}),
                 ('State', {'fields': ('is_active',
                                       'is_admin',)}),
                 (None, {'fields': ('date_joined',)}),
                 )


admin.site.register(User, UserAdmin)
