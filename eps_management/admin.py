from django.contrib import admin

# Register your models here.

from .models import EpsLogSource, EpsTotal, EpsManagement, Notification, EpsERCAllMcafee, EPS_DS_Collection_Rate, EPS_DS_Parsing_Rate


class EpsAdmin(admin.ModelAdmin):
    list_display = ['id_epslogsource', 'created_date', 'name_log_source', 'company', 'count_range', 'count_intervale']
    list_filter = ['company']

admin.site.register(EpsLogSource, EpsAdmin)



class EpsTotalAdmin(admin.ModelAdmin):
    list_display = ['id_epstotal', 'created_date', 'company', 'count_range', 'count_intervale']
    list_filter = ['company']


admin.site.register(EpsTotal, EpsTotalAdmin)



class EpsManagementAdmin(admin.ModelAdmin):
    list_display = ['id_epsmanagement', 'eps_limit', 'company']
    list_filter = ['company']


admin.site.register(EpsManagement, EpsManagementAdmin)



class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id_notification', 'eps_management', 'company', 'eps_notification']
    list_filter = ['company']


admin.site.register(Notification, NotificationAdmin)


class EpsERCAllMcafeeAdmin(admin.ModelAdmin):
    list_display = ['id_epsercallmcafee', 'company', 'erc_collection_rate', 'erc_parsing_rate', 'name_file']
    list_filter = ['company']
    list_max_show_all = 1000
    list_per_page = 1000


admin.site.register(EpsERCAllMcafee, EpsERCAllMcafeeAdmin)





class EPS_DS_Collection_RateAdmin(admin.ModelAdmin):
    list_display = ['id_epsdscollectionrate', 'company', 'ds_collection_rate', 'epsercallmcafee', "log_source", 'name_file']
    list_filter = ['company']
    list_max_show_all = 1000
    list_per_page = 1000

admin.site.register(EPS_DS_Collection_Rate, EPS_DS_Collection_RateAdmin)



class EPS_DS_Parsing_RateAdmin(admin.ModelAdmin):
    list_display = ['id_epsdsparsingrate', 'company', 'ds_parsing_rate', 'epsercallmcafee', "log_source", 'name_file']
    list_filter = ['company']
    list_max_show_all = 1000
    list_per_page = 1000

admin.site.register(EPS_DS_Parsing_Rate, EPS_DS_Parsing_RateAdmin)




