from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=120)
    price = models.IntegerField(verbose_name="Prix")

    def __str__(self):
        return self.name