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
