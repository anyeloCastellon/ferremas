from django.db import models

# Create your models here.
from base.models import BaseModel


class EpsLogSource(BaseModel):
    id_epslogsource = models.AutoField(primary_key = True)

    name_log_source = models.ForeignKey(
        "log_source.LogSource",
        on_delete=models.CASCADE,
        db_column='id_name_log_source'
        )

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    count_range = models.PositiveIntegerField(default=0)

    count_intervale = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)



    def __str__(self):
        return f'{self.name_log_source} {self.company} {self.count_range}'

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EpsLogSource'
        verbose_name_plural = 'EpsLogSource'




class EpsTotal(BaseModel):
    id_epstotal = models.AutoField(primary_key = True)

    eps_log_source = models.ManyToManyField(
        'eps_management.EpsLogSource',
    )

    notification = models.ManyToManyField(
        'eps_management.Notification',
    )

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    count_range = models.PositiveIntegerField(default=0)

    count_intervale = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)


    def __str__(self):
        return f'{self.company} {self.count_range}'

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EpsTotal'
        verbose_name_plural = 'EpsTotal'





class EpsManagement(BaseModel):
    id_epsmanagement = models.AutoField(primary_key = True)

    eps_limit = models.PositiveIntegerField(default=0)

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )


    def __str__(self):
        return f'{self.company} {self.eps_limit}'

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EpsManagement'
        verbose_name_plural = 'EpsManagement'




class Notification(BaseModel):
    id_notification = models.AutoField(primary_key = True)

    eps_management = models.ForeignKey(
        "eps_management.EpsManagement",
        on_delete=models.CASCADE,
        db_column='id_eps_management'
        )

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )
    
    eps_notification = models.PositiveIntegerField(default=50)


    def __str__(self):
        return f'{self.company} {self.eps_management} {self.eps_notification}'

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

