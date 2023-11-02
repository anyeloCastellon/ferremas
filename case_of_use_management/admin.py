from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.


from .models import TypeRule, TypeTech, SignatureCiber, CaseUse


# Register your models here.
class TypeRuleAdmin(admin.ModelAdmin):
    list_display = ['id_type_rule', 'name_type_rule', 'enabled']

admin.site.register(TypeRule, TypeRuleAdmin)


class TypeTechAdmin(admin.ModelAdmin):
    list_display = ['id_type_tech', 'name_type_tech', 'enabled']

admin.site.register(TypeTech, TypeTechAdmin)


class SignatureCiberAdmin(admin.ModelAdmin):
    list_display = ['id_signature_ciber', 'name_signature_ciber', 'enabled']

admin.site.register(SignatureCiber, SignatureCiberAdmin)


class CaseUseCiberAdmin(admin.ModelAdmin):
    list_display = ['id_case_of_use', 'name_case_of_use', 'get_company_names', 'get_incident_names', 'count_companies', 'enabled']

    def get_company_names(self, obj):
        company_names = '\n'.join([company.name for company in obj.company.all()])
        return mark_safe(company_names.replace('\n', '<br>'))


    get_company_names.short_description = 'Nombres de Empresas Asociadas'


    def get_incident_names(self, obj):
        incident_names = '\n'.join([incident.name_incident for incident in obj.incident.all()])
        return mark_safe(incident_names.replace('\n', '<br>'))

    get_incident_names.short_description = 'Incidentes Asociados'


    def count_companies(self, obj):
        # Obj es la instancia actual de CaseUse
        return obj.company.count()  # "company" es el nombre predeterminado de la relación ManyToMany con Company

    count_companies.short_description = '# Empresas Asociadas'  # Cambia el encabezado en la vista del administrador





admin.site.register(CaseUse, CaseUseCiberAdmin)