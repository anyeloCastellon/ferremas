from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ['username', 'email']
    fieldsets = UserAdmin.fieldsets

admin.site.register(User, UserAdmin)

