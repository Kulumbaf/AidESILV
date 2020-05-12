from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        '''
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