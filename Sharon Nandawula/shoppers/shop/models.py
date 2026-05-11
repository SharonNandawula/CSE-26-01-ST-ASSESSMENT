from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    color = models.CharField(max_length=100, blank=True)

def __str__(self):
        return self.name