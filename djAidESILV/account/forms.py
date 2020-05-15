from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'prenom',
            'nom',
            'code_postal',
            'ville',
            'num_rue',
            'nom_rue',
            'tel',
            'foyer',
            'bebes',
        )