from __future__ import unicode_literals

from django.db import models

CATEGORY_CHOICES = (
    ('A', 'Alimentation'),
    ('P', 'Pharmacie'),
    ('Q', 'Quotidien'),
    ('NA', 'Non-attribué')
)

class Product(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=120)
    price = models.IntegerField(verbose_name="Prix")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='NA', verbose_name='Catégorie')
    baby_product = models.BooleanField(default=False, verbose_name='Produit pour enfant')

    def __str__(self):
        return self.name