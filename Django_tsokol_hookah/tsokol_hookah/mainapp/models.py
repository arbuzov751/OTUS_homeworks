from django.db import models


class MainModel(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    price = models.CharField(max_length=64, blank=True, null=True)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'главная модель'
        verbose_name_plural = 'главные модели'
