from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, Company, TypeCompany, SIEM


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ['username', 'email']
    fieldsets = UserAdmin.fieldsets



class UserAdminServer(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_admin', 'is_server', 'is_root', ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id_company', 'name', 'type_company', 'enabled', 'domain_id_qradar', 'siem', 'is_search']
    list_filter = ['siem', 'enabled', 'is_search']

class TypeCompanyAdmin(admin.ModelAdmin):
    list_display = ['id_typecompany', 'name', 'enabled',]


class SIEMAdmin(admin.ModelAdmin):
    list_display = ['id_siem', 'name', 'enabled',]


class GeolocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_v4', 'latitude',  'longitude', 'country_code_plural', 'country_code_singular', 'country_name']
    list_filter = ['country_name']

class PathURLAdmin(admin.ModelAdmin):
    list_display = ['id', 'geolocation', 'user', 'path_back',  'path_front', 'http_referer', 'http_sec_ch_ua', 'http_user_agent', 'created_date']
    list_filter = ['user', 'geolocation']

admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(TypeCompany, TypeCompanyAdmin)
admin.site.register(SIEM, SIEMAdmin)
