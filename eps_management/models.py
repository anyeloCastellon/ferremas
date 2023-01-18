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






class EpsERCAllMcafee(BaseModel):
    id_epsercallmcafee = models.AutoField(primary_key = True)


    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    erc_collection_rate = models.PositiveIntegerField(default=0)
    erc_parsing_rate = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField('Fecha de Creación')

    name_file = models.CharField(null=True, blank=True, max_length=2000)

    def __str__(self):
        return f'{self.company} {self.erc_collection_rate} {self.erc_parsing_rate}'


    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EpsERCAllMcafee'
        verbose_name_plural = 'EpsERCAllMcafee'





class EPS_DS_Collection_Rate(BaseModel):
    id_epsdscollectionrate = models.AutoField(primary_key = True)

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    ds_collection_rate = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField('Fecha de Creación')

    epsercallmcafee = models.ForeignKey(
        "eps_management.EpsERCAllMcafee",
        on_delete=models.CASCADE,
        related_name='eps_ds_collection_rate_epsercallmcafee'
        )
    name_file = models.CharField(null=True, blank=True, max_length=2000)

    log_source = models.ForeignKey(
        "log_source.LogSource",
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.company} {self.ds_collection_rate} {self.log_source}'


    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EPS_DS_Collection_Rate'
        verbose_name_plural = 'EPS_DS_Collection_Rate'



class EPS_DS_Parsing_Rate(BaseModel):
    id_epsdsparsingrate = models.AutoField(primary_key = True)

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    ds_parsing_rate = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField('Fecha de Creación')
    name_file = models.CharField(null=True, blank=True, max_length=2000)

    epsercallmcafee = models.ForeignKey(
        "eps_management.EpsERCAllMcafee",
        on_delete=models.CASCADE,
        related_name='eps_ds_parsing_rate_epsercallmcafee'
        )

    log_source = models.ForeignKey(
        "log_source.LogSource",
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.company} {self.ds_parsing_rate} {self.log_source}'


    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'EPS_DS_Parsing_Rate'
        verbose_name_plural = 'EPS_DS_Parsing_Rate'