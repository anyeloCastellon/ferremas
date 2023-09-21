from django.contrib import admin

# Register your models here.


from .models import Module, LogSource
# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id_module', 'name_module', 'enabled']

admin.site.register(Module, ModuleAdmin)


class LogSourceAdmin(admin.ModelAdmin):
    list_display = ['id_datasource', 'name_log_source', 'enabled', 'company', 'number_log_source', 'ip', 'seguir_escalando', 'estado_datasource']
    list_filter = ['company', 'seguir_escalando']
    list_editable = ['seguir_escalando', 'estado_datasource']

admin.site.register(LogSource, LogSourceAdmin)