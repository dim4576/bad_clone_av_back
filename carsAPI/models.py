import os
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Cars(models.Model):
    sellerUsername = models.TextField(
        verbose_name='username продавца'
    )
    adventType = models.CharField(
        verbose_name='тип транспорта',
        max_length=20
    )
    priceUSD = models.FloatField(
        verbose_name='цена в долларах'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    sellerName = models.TextField(
        verbose_name='Имя продавца'
    )
    locationName = models.TextField(
        verbose_name='населённый пункт продажи'
    )
    year = models.IntegerField(
        verbose_name='год выпуска'
    )
    vin = models.CharField(
        verbose_name='вин код ТС',
        max_length=30
    )
    brand = models.TextField(
        verbose_name='марка машины'
    )
    model = models.TextField(
        verbose_name='модель машины'
    )
    generation = models.TextField(
        verbose_name='поколение модели'
    )
    engine_capacity = models.TextField(
        verbose_name='объём двигателя'
    )
    engine_type = models.TextField(
        verbose_name='тип двигателя'
    )
    transmition_type = models.TextField(
        verbose_name='тип коробки передач'
    )

class Photos(models.Model):
    car_id = models.ForeignKey(
        Cars,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    photo = models.TextField(
        verbose_name='сылка на фото',
    )



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
