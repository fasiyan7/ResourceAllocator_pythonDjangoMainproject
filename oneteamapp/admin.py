from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth import get_user_model
from .models import *


CustomUserModel = get_user_model()

class CustomUserAdmin(UserAdmin):
   fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'user_type','profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)		
admin.site.register(Staff)
admin.site.register(Laptop)
admin.site.register(Hall)
admin.site.register(Batches)
admin.site.register(Post)
admin.site.register(Assignment)









 