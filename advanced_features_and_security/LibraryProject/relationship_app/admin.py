from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  model = CustomUser
  
  fieldsets = UserAdmin.fieldsets + (
    ("Additional Info", {
      "fields": ("date_of_birth", "profile_photo"),
    }),
  )
  
  list_display = ("username", "email", "date_of_birth", "is_staff")