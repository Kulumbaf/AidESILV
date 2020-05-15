from django.conf.urls import url
from .views import my_profile, signup

app_name = 'account'

urlpatterns = [
    url(r'^inscription/$', signup, name='signup'),
    url(r'^moi/$', my_profile, name='my_profile')
]