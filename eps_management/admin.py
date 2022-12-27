from django.contrib import admin

# Register your models here.

from .models import EpsLogSource, EpsTotal, EpsManagement, Notification


class EpsAdmin(admin.ModelAdmin):
    list_display = ['id_epslogsource', 'created_date', 'name_log_source', 'company', 'count_range', 'count_intervale']

admin.site.register(EpsLogSource, EpsAdmin)



class EpsTotalAdmin(admin.ModelAdmin):
    list_display = ['id_epstotal', 'created_date', 'company', 'count_range', 'count_intervale']

admin.site.register(EpsTotal, EpsTotalAdmin)



class EpsManagementAdmin(admin.ModelAdmin):
    list_display = ['id_epsmanagement', 'eps_limit', 'company']

admin.site.register(EpsManagement, EpsManagementAdmin)



class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id_notification', 'eps_management', 'company', 'eps_notification']

admin.site.register(Notification, NotificationAdmin)


