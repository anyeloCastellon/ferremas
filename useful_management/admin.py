from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'motivo', 'mensaje', 'usuario',)
    list_filter = ('motivo', 'usuario',)
    search_fields = ('nombre_completo', 'mensaje', 'usuario__username')

    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Contacto, ContactoAdmin)
