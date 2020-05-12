from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def modify_profile(request): #à modifier !
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
    else:
        form = RegistrationForm()
    return render(request, 'registration/modify_profile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})