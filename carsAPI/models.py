import os
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Cars(models.Model):
    brand = models.CharField(
        verbose_name='марка',
        max_length=60
    )
    model = models.CharField(
        verbose_name='модель',
        max_length=60
    )
    year = models.IntegerField(
        verbose_name='год выпуска'
    )
    price = models.IntegerField(
        verbose_name='цена в долларах США'
    )
    photos = models.ImageField(
        verbose_name='фото машины',
        upload_to='./static/'
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
