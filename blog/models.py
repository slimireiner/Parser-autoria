from django.db import models
from django.urls import reverse

class Car(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выпуска')
    race = models.IntegerField(verbose_name='Пробег')
    type_fuel = models.CharField(max_length=50, verbose_name='Тип топлева')
    type_of_drive = models.CharField(max_length=50, verbose_name='Тип трансмисси')
    drive_unit = models.CharField(max_length=50, verbose_name='Привод')
    body_type = models.CharField(max_length=50, verbose_name='Тип кузова')
    current_usd = models.IntegerField(verbose_name='Цена в $')
    current_eur = models.IntegerField(verbose_name='Цена в Евр')
    current_grn = models.IntegerField(verbose_name='Цена в Грн')
    city = models.CharField(max_length=50, verbose_name='Город/Продавец')
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Авто'

class Try(models.Model):
    info = models.TextField(max_length= 50)
    info1 = models.IntegerField()