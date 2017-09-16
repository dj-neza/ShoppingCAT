from django.shortcuts import render

# Create your views here.

def home(request):
	if request.user.is_authenticated():
		return render(request, 'index.html')

	return render(request, 'home.html')

def index(request):
	return render(request, 'home.html')
