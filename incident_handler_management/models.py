from django.db import models

# Create your models here.

from base.models import BaseModel



class TypeIncident(BaseModel):
    id_type_incident = models.AutoField(primary_key = True)
    name_type_incident = models.CharField(max_length=256, blank=False, null=False)


    def __str__(self):
        return self.name_type_incident

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'TypeIncident'
        verbose_name_plural = 'TypeIncident'



class Incident(BaseModel):
    id_incident = models.AutoField(primary_key = True)
    name_incident = models.CharField(max_length=256, blank=False, null=False)

    type_incident = models.ForeignKey(
        'incident_handler_management.TypeIncident',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name_incident

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'Incident'
        verbose_name_plural = 'Incident'

