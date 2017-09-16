from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import *


@csrf_protect
def home(request):
	if request.user.is_authenticated():
		return render(request, 'index.html')

	return render(request, 'home.html')

# sign in
@csrf_protect
def index(request):
	form = SignIn(request.POST or None)

	return render(request, 'home.html', {'form': form})
