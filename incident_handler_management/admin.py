from django.contrib import admin

# Register your models here.


from .models import TypeIncident, Incident


# Register your models here.
class TypeIncidentAdmin(admin.ModelAdmin):
    list_display = ['id_type_incident', 'name_type_incident', 'enabled']

admin.site.register(TypeIncident, TypeIncidentAdmin)


class IncidentAdmin(admin.ModelAdmin):
    list_display = ['id_incident', 'name_incident', 'type_incident', 'number_of_use_cases', 'enabled']
    list_editable = ['number_of_use_cases']

admin.site.register(Incident, IncidentAdmin)