from django.db import models

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
        verbose_name='фото машины'
    )
