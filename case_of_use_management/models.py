from django.db import models

# Create your models here.
from base.models import BaseModel



class TypeRule(BaseModel):
    id_type_rule = models.AutoField(primary_key = True)
    name_type_rule = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name_type_rule

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'TypeRule'
        verbose_name_plural = 'TypeRule'



class TypeTech(BaseModel):
    id_type_tech = models.AutoField(primary_key = True)
    name_type_tech = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name_type_tech

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'TypeTech'
        verbose_name_plural = 'TypeTech'



class SignatureCiber(BaseModel):
    id_signature_ciber = models.AutoField(primary_key = True)
    name_signature_ciber = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name_signature_ciber

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'SignatureCiber'
        verbose_name_plural = 'SignatureCiber'



class CaseUse(BaseModel):
    id_case_of_use = models.AutoField(primary_key = True)
    name_case_of_use = models.CharField(max_length=1256, blank=False, null=False)
    observation = models.TextField(default="")
    is_created = models.BooleanField(default=True)


    type_rule = models.ManyToManyField(
        'case_of_use_management.TypeRule',
        blank=True,
    )


    type_tech = models.ManyToManyField(
        'case_of_use_management.TypeTech',
        blank=True,
    )


    signature_ciber = models.ManyToManyField(
        'case_of_use_management.SignatureCiber',
        blank=True,
    )


    siem = models.ManyToManyField(
        'user_management.SIEM',
        blank=True,
    )


    company = models.ManyToManyField(
        'user_management.Company',
        blank=True,
    )


    incident = models.ManyToManyField(
        'incident_handler_management.Incident',
        blank=True,
    )


    type_incident = models.ManyToManyField(
        'incident_handler_management.TypeIncident',
        blank=True,
    )


    def __str__(self):
        return self.name_case_of_use

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'CaseUse'
        verbose_name_plural = 'CaseUse'
