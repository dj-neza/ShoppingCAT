from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^home/$", views.home, name="home"),
	url(r'^log_out/', views.log_out, name='log_out'), 
	url(r'^loadInspirationImage/', views.loadInspirationImage, name='loadInspirationImage'), 
]