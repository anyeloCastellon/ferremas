from django.contrib import admin

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
    list_display = ['id_case_of_use', 'name_case_of_use', 'enabled']

admin.site.register(CaseUse, CaseUseCiberAdmin)