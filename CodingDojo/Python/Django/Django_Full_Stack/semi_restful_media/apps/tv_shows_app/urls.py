#---------------------------------------------------
# tv_shows_app urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.viewShows),
    url(r'^newShow$', views.newShow),
    url(r'^createShow/$', views.createShow),
    url(r'^viewShows$', views.viewShows),
    url(r'^viewShow/(?P<id>\d+)$', views.viewShow),
    url(r'^editShow/(?P<id>\d+)$', views.editShow),
    url(r'^updateShow/(?P<id>\d+)$', views.updateShow),
    url(r'^removeShow/(?P<id>\d+)$', views.removeShow),
]
