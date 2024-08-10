from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from .validations import phone_validate
from .managers import CustomUserManager, ActiveUserManager
from apps.general.enums.regions import RegionChoices
from apps.general.enums.districts import DistrictChoices


class CustomUser(AbstractUser):
    username = None
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'  # Should be a string, not a list
    objects = CustomUserManager()
    active_objects = ActiveUserManager()

    full_name = models.CharField(max_length=75, blank=True, null=True)

    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    phone_number2 = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)

    region = models.PositiveSmallIntegerField(choices=RegionChoices.choices, blank=True, null=True)
    district = models.PositiveSmallIntegerField(choices=DistrictChoices.choices, blank=True, null=True)

    balance = models.DecimalField(max_digits=10, decimal_places=1, help_text='In UZS', default=0)

    is_deteted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.phone_number}'

    def save(self, *args, **kwargs):
        if self.pk:
            self.phone_number2 = self.phone_number
        return super().save(*args, **kwargs)
