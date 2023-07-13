from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    name = models.CharField(max_length=15)
    phone_number = PhoneNumberField(unique=True)
    verification_code = models.CharField(max_length=4, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.pk} - {self.phone_number}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
