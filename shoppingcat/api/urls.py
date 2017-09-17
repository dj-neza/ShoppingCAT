# api/urls.py

from django.conf.urls import url, include
from . import views
from .views import CreateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = {
    url(r'^capi/myclothing/$', CreateView.as_view(), name="create"),
    url(r'^capi/myclothing/(?P<pk>[0-9]+)$', views.myclothing_detail),
    url(r'^capi/myclothing/(?P<username>\w+)/$', views.myclothing_user),
    #url(r'^capi/inspiration/(?P<username>\w+)/$', views.inspirations_user),
    #url(r'^capi/inspiration/(?P<pk>[0-9]+)$', views.inspirations_detail),
    url(r'^capi/inspiration/$', views.InspirationList.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)