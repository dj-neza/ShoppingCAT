from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^home/$", views.home, name="home"),
	url(r'^log_out/', views.log_out, name='log_out'), 
	url(r'^addCloset/(?P<r_id>[0-9]+)/$', views.addCloset, name='addCloset'),
	url(r'^addWish/(?P<name>[0-9]+)/(?P<category>[%&.+ \w]+)/(?P<productURL>[%&.+ \w]+)/(?P<imageURL>[%&.+ \w]+)/(?P<price>[%&.+ \w]+)/(?P<SKUcode>[%&.+ \w]+)$', views.addWish, name='addWish'),
]