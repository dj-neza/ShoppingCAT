from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import *


def get_user_data(user):
	clothes = MyClothing.objects.filter(user=user)
	recommendations = Recommendation.objects.filter(user=user)
	inspirations = Inspiration.objects.filter(user=user)
	return clothes, recommendations, inspirations

@csrf_protect
def home(request):
	
	# user is signed in
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user.username)
		c, r, i = get_user_data(user)
		
		return render(request, 'index.html', {'name': request.user.first_name, 'clothes': c, 'recommendations': r, 'inspirations': i})

	# user not signed in
	else:
		form = SignIn()
		return render(request, 'home.html', {'form': form})


# sign in
@csrf_protect
def index(request):

	# user is already signed in
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user.username)
		c, r, i = get_user_data(user)
		for ind in i:
			print(ind)
		return render(request, 'index.html', {'name': request.user.first_name, 'clothes': c, 'recommendations': r, 'inspirations': i})

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
					user = User.objects.get(username=request.user.username)
					c = get_user_data(user)
					return render(request, 'index.html', {'name': user.first_name, 'clothes': c})

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
			newInsp = form.save(commit=False)
			newInsp.user = request.user;
			newInsp.save()
		else:
			print("Photo not saved ")

	i = get_user_data(request.user)	

	return render(request, 'loadInspirationImage.html', {'form': form, 'name': request.user.first_name, 'inspirations':i})

# get inspirations and return list of inspirations
def loadRecs(request):
	r = get_user_data(request.user)

	return render(request, 'myrecommendations.html', {'name': request.user.first_name, 'recommendations': r})

