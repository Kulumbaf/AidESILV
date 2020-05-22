from django.conf.urls import url

from .views import (
    product_list, 
    alimentation,
    pharmacie,
    quotidien,
    piechart
    )

app_name = 'products'

urlpatterns = [
    url(r'^liste$', product_list, name='product-list'),
    url(r'^alimentation$', alimentation, name="alimentation"),
    url(r'^pharmacie$', pharmacie, name="pharmacie"),
    url(r'^quotidien$', quotidien, name="quotidien"),
    url(r'^piechart$', piechart, name="piechart"),
]