#---------------------------------------------------
# blog urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'blog-home'),
    url(r'^about/$', views.about, name = 'blog-about'),
]
