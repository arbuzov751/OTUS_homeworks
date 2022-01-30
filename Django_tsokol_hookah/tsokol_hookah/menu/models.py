from django.db import models


class Menu(models.Model):
    product_name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    price = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}: {self.product_name} = {self.price}р'
