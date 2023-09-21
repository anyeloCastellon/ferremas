from django.db import models

# Create your models here.

from base.models import BaseModel

class Module(BaseModel):
    id_module = models.AutoField(primary_key = True)
    name_module = models.CharField(max_length=256, blank=False, null=False)


    def __str__(self):
        return self.name_module

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'Module'
        verbose_name_plural = 'Module'

    


class LogSource(BaseModel):
    id_datasource = models.AutoField(primary_key = True)

    module = models.ManyToManyField(
        'log_source.Module',
        blank=True,
    )

    name_log_source = models.CharField(max_length=256, blank=False, null=False)

    number_log_source = models.BigIntegerField(blank=True, null=True)

    ip = models.CharField(max_length=15, blank=True, null=True)
    seguir_escalando = models.BooleanField(default = True)
    estado_datasource = models.BooleanField(default = True)
    zona_horaria = models.CharField(max_length=50, choices=[('UTC', 'UTC'), ('GTM-3', 'GTM-3'), ('GTM-4', 'GTM-4')], null=True, blank=True, default="GTM-3")

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.name_log_source}'

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'LogSource'
        verbose_name_plural = 'LogSource'






