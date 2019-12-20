from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Property

# Register your models here.

# define and inline admin descriptor for Profile model
# refer to django docs -> extending-user
class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name_plural = 'profile'

# define a new User admin
class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInline,)

# re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Property)