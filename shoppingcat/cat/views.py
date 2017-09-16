from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import *


@csrf_protect
def home(request):
	
	# user is signed in
	if request.user.is_authenticated():
		return render(request, 'index.html', {'name': request.user.first_name})

	# user not signed in
	else:
		form = SignIn()
		return render(request, 'home.html', {'form': form})


# sign in
@csrf_protect
def index(request):

	# user is already signed in
	if request.user.is_authenticated():
		return render(request, 'index.html', {'name': request.user.first_name})

	else:
		if request.method == "POST":
			form = SignIn(request.POST or None)

			if form.is_valid():
				data = form.cleaned_data
				username = data["username"]
				password = data["password"]
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					return render(request, 'index.html', {'name': user.first_name})

		else:
			form = SignIn()

		return render(request, 'home.html', {'form': form})

# log out
def log_out(request):

	if request.user.is_authenticated:
		logout(request)

	return redirect('index')

# inspiration load image
def loadInspirationImage(request):
	form = LoadInspirationImage()
	if request.method == 'POST':
		form = LoadInspirationImage(request.POST, request.FILES)
		if form.is_valid():
			cl = form.cleaned_data
			print(cl)
			#newInsp = form.save(commit=False)
			#newInsp.user = request.user;
			#newInsp.save()
		else:
			print("Photo not saved ")		
	return render(request, 'loadInspirationImage.html', {'form': form, 'name': request.user.first_name})


