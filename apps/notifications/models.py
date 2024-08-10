from django.db import models
from django.conf import settings


class NotificationType(models.Model):
    class Type(models.IntegerChoices):
        DISCOUNT = 0
        ON_BOOKING = 1
        REMINDER = 2

    section = models.PositiveSmallIntegerField(choices=Type.choices, unique=True)
    image = models.ImageField(upload_to='notifications/images')


class Notification(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    section = models.PositiveSmallIntegerField(choices=NotificationType.Type.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
