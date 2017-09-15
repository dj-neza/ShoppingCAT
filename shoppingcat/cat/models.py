from django.db import models
from django.utils import timezone

# Create your models here.
class MyClothes(models.Model):
	name = models.TextField()
	user = models.ForeignKey('auth.User')

	def __str__(self):
		return self.name