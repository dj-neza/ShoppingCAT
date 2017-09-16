from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout

from .forms import *


@csrf_protect
def home(request):
	#if request.user.is_authenticated():
	return render(request, 'index.html')

	#return render(request, 'home.html')

# sign in
@csrf_protect
def index(request):
	form = SignIn(request.POST or None)

	if form.is_valid():
		data = form.cleaned_data
		username = data["email"]
		password = data["password"]
		user = authenticate(username=username, password=password)
		login(request, user)

	return render(request, 'home.html', {'form': form})

# log out
def logout(request):
	if request.user.is_authenticated:
		logout(request)

	form = SignIn(request.POST or None)

	return render(request, 'home.html', {'form':form})
