from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from shopping_cart.models import Order
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def my_profile(request):
	my_user_profile = UserProfile.objects.filter(email=request.user.email).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)