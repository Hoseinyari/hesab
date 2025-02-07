from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager , PermissionsMixin
from django.utils import  timezone


class AccountManger(UserManager):
    def _create_user(self, phone_number : str | None, password : str | None, **extra_fields):
        if not len(phone_number) == 11 or not phone_number.isdigit() or not phone_number.startswith("09"):
            raise ValueError("شماره همراه وارد شده صحیح نیست (باید ۱۱ رقم باشد و با ۰۹ شروع شود )!!!")
        Account = self.model(phone_number=phone_number, **extra_fields)
        Account.set_password(password)

        Account.save(using=self._db)

        return Account

    def create_user(self, phone_number :str | None, password :str | None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number :str | None, password : str | None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(phone_number, password, **extra_fields)




class Account(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, blank=True, unique=True, default="")

    username = models.CharField(max_length=50)

    email = models.EmailField(max_length=200, blank=True, default="")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = AccountManger()

    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = 'Accounts'

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)

