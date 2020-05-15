from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('core.urls')),
    url(r'^account/', include('account.urls', namespace='account')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart'))
]