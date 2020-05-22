from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('core.urls')),
    url(r'^compte/', include('account.urls', namespace='account')),
    path('comptes/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^ravitaillement/', include('products.urls', namespace='products')),
    url(r'^panier/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^alimentation/', include('products.urls', namespace='alimentation')),
    url(r'^pharmacie/', include('products.urls', namespace='pharmacie')),
    url(r'^quotidien/', include('products.urls', namespace='quotidien')),
    url(r'^piechart/', include('products.urls', namespace="piechart")),
]