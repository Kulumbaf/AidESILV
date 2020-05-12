from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import UserProfile

def home(request):
    count = UserProfile.objects.count()
    return render(request, 'home.html', {'count': count})