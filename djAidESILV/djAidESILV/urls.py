from django.contrib import admin
from django.urls import path, include
from account.views import modify_profile

urlpatterns = [
    path('', include('core.urls')),
    path('signup/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('modify_profile/', modify_profile, name="modify_profile"),
    path('admin/', admin.site.urls),
]
