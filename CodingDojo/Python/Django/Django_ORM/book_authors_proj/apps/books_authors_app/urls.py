#---------------------------------------------------
# books_authors_app urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
