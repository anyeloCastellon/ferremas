from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate

from base.models import BaseModel


class User(AbstractUser):
    username = models.CharField("username", max_length=55, unique=True)
    email = models.CharField("E-mail", max_length=100)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('')

    @staticmethod
    def login(request, username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            return None
        else:
            return user

    class Meta:
        verbose_name = "User"
        ordering = ['pk']


class TypeCompany(BaseModel):
    id_typecompany = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ['pk']
        verbose_name_plural = "TypeCompanies"

    def __str__(self):
        return self.name



class SIEM(BaseModel):
    id_siem = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ['pk']
        verbose_name_plural = "SIEM"

    def __str__(self):
        return self.name



class Company(BaseModel):
    id_company= models.AutoField(primary_key = True)

    name = models.CharField(max_length=50, null=False)

    is_search = models.BooleanField(default=True)

    domain_id_qradar = models.PositiveSmallIntegerField(null=True, blank=True)


    type_company = models.ForeignKey(
        "user_management.TypeCompany",
        on_delete=models.CASCADE
        )

    siem = models.ForeignKey(
        "user_management.SIEM",
        on_delete=models.CASCADE,
        null=True, 
        blank=True
        )

    class Meta:
        ordering = ['pk']
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

