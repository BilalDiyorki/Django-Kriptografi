from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUserModel

@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display= ('first_name','last_name','username', 'email','public_key')
