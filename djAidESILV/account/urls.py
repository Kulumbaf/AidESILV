from django.conf.urls import url
from .views import my_profile, signup

app_name = 'account'

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^me/$', my_profile, name='my_profile')
]