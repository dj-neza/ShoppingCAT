from django.db import models
from django.utils import timezone

# Create your models here.
class Clothing(models.Model):
	name = models.TextField()
	category = models.TextField()
	productURL = models.URLField(max_length=500)
	imageURL = models.URLField(max_length=500)
	price = models.FloatField()
	SKUcode = models.TextField()

	class Meta:
		abstract = True

	def __str__(self):
		return self.name


class MyClothing(Clothing):
	user = models.ForeignKey('auth.User')


class Inspiration(models.Model):
	user = models.ForeignKey('auth.User')
	image = models.FileField(upload_to='inspirations/')

class Recommendation(Clothing):
	user = models.ForeignKey('auth.User')
	inspiration = models.ForeignKey('Inspiration')