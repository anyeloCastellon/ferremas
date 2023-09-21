from django.contrib import admin
from .models import RegistroHistorico
import csv
from django.http import HttpResponse
from django.utils import timezone
import datetime

# Register your models here.
class RegistroHistoricoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'estado', 'escalado_a', 'comentario', 'name_log_source', 'company']
    list_filter = ['company']
    list_editable = ['estado', 'escalado_a']
    actions = ['export_to_csv']

    def export_to_csv(modeladmin, request, queryset):
        meta = modeladmin.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.verbose_name}.csv'
        writer = csv.writer(response)

        # Escribir los nombres de las columnas
        headers = [field.name for field in meta.fields]
        writer.writerow(headers)

        # Escribir los datos
        for obj in queryset:
            row = []
            for field in meta.fields:
                value = getattr(obj, field.name)
                # Si el valor es un objeto datetime y es timezone-aware, convertirlo a la zona horaria local
                if isinstance(value, datetime.datetime) and timezone.is_aware(value):
                    value = timezone.localtime(value)
                row.append(value)
            writer.writerow(row)


        return response


admin.site.register(RegistroHistorico, RegistroHistoricoAdmin)