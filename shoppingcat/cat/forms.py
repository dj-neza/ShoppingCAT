from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class SignIn(forms.Form):

	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)
		
		if not user or not user.is_active:
			raise forms.ValidationError("Incorrect username or password")
		return self.cleaned_data

class LoadInspirationImage(forms.ModelForm):
	class Meta: 
		model = Inspiration
		fields = [
			'image'
		]

