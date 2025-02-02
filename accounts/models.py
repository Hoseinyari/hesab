from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import  timezone
from django.conf import settings


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100 , blank=True , default="")
    phone_number = models.CharField(max_length=20, blank=True, unique=True, default="")

    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = 'Accounts'

       
    def __str__(self) -> str:
        return f"{self.username} : {self.phone_number}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True, blank=True)

