from django.contrib import admin
from .models import Contact, User, Product
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('email', 'id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')

    fieldsets = (
        (None, {
            "fields": (
                'email',
                'image',
                'password',
                'username',
                'first_name',
                'last_name',
                'address'
            ),
        }),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ('wide'),
            "fields": (
                'email',
                'first_name',
                'last_name',
                'username',
                'image',
                'address',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )

    ordering = ('email',)
    
    

# admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Product)

