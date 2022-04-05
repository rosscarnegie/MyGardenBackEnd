from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Import your models here.
from .models.gardeners import Gardener
from .models.plants import Plant


class UserAdminConfig(UserAdmin):
    search_fields =('email', 'username',)
    list_filter = ('is_active', 'is_staff', 'is_superuser',)
    ordering =('id',)
    list_display=('id', 'username', 'email', 'zipcode', 'zone', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        ('User Info', {'fields': ('email', 'username', 'is_active', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
        ('User Provided Information', {'fields': ('zone', 'about')}),
    )

    formfield_overides = {
        # Leaving blank for later
        Gardener.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 30})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'zipcode', 'is_staff', 'is_superuser', 'password1', 'password2',)
        }),
    )


# Register your models here.
admin.site.register(Gardener)
admin.site.register(Plant)