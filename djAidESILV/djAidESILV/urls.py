from django.contrib import admin
from django.urls import path, include

from djAidESILV.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name='secret'),
    path('admin/', admin.site.urls),
]
