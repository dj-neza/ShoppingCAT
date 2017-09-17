from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = "dhqd5qhlk",
    api_key = "423479666628262",
    api_secret = "ou30z6O3KL46XANlIOZ3JxiWzbE"
)


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
		if request.method == 'POST':
			form = LoadInspirationImage(request.POST, request.FILES)
			print(form)
			if form.is_valid():
				cl = form.cleaned_data
				print(cl)
				lal = cloudinary.uploader.upload(cl['image'])
				print(lal['secure_url'])
				newInsp = Inspiration(
					image=lal['secure_url'],
					user=request.user)
				newInsp.save()
			else:
				print("Photo not saved ")
		else:
			form = LoadInspirationImage()
		return render(request, 'index.html', {'name': request.user.first_name, 'form': form, 'clothes': c, 'recommendations': r, 'inspirations': i})

	# user not signed in
	else:
		form2 = SignIn()
		return render(request, 'home.html', {'form2': form2})


# sign in
@csrf_protect
def index(request):

	# user is already signed in
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user.username)
		c, r, i = get_user_data(user)
		for ind in i:
			print(ind)
		form = LoadInspirationImage()
		if request.method == 'POST':
			form = LoadInspirationImage(request.POST, request.FILES)
			if form.is_valid():
				cl = form.cleaned_data
				print(cl)
				lal = cloudinary.uploader.upload(cl['image'])
				print(lal['secure_url'])
				newInsp = Inspiration(
					image=lal['secure_url'],
					user=request.user)
				newInsp.save()
			else:
				print("Photo not saved ")
		return render(request, 'index.html', {'name': request.user.first_name, 'form': form, 'clothes': c, 'recommendations': r, 'inspirations': i})

	else:
		if request.method == "POST":
			form2 = SignIn(request.POST or None)
			form = LoadInspirationImage()
			if form2.is_valid():
				data = form2.cleaned_data
				username = data["username"]
				password = data["password"]
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					user = User.objects.get(username=request.user.username)
					c, r, i = get_user_data(user)
					return render(request, 'index.html', {'name': user.first_name, 'form': form, 'clothes': c, 'recommendations': r, 'inspirations': i})

		else:
			form2 = SignIn()

		return render(request, 'home.html', {'form2': form2})

# log out
def log_out(request):

	if request.user.is_authenticated:
		logout(request)

	return redirect('index')
