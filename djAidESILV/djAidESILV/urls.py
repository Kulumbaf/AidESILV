from django.contrib import admin
from django.urls import path

from djAidESILV.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
]