from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^$', views.new),
    url(r'^$', views.create),
    url('/<num>', views.show),
    url('<num>/delete', views.delete),
]