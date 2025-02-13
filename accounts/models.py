from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager , PermissionsMixin
from django.utils import  timezone


class AccountManger(UserManager):
    def _create_user(self, username : str | None, password : str | None, **extra_fields):
        Account = self.model(username=username, **extra_fields)
        Account.set_password(password)

        Account.save(using=self._db)

        return Account

    def create_user(self, username :str | None, password :str | None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username :str | None, password : str | None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(username, password, **extra_fields)




class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    
    email = models.EmailField(max_length=200, blank=True, default="")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = AccountManger()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = 'Accounts'

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)

