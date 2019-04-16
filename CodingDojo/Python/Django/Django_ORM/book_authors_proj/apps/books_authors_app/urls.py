#---------------------------------------------------
# books_authors_app urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.showBooks),
    url(r'^createBook$', views.createBook),
    url(r'^viewBook/(?P<id>\d+)$', views.viewBook),
    url(r'^removeBook/(?P<id>\d+)$', views.removeBook),

    url(r'^authors/$', views.showAuthors),
    url(r'^createAuthor$', views.createAuthor),
    url(r'^viewAuthor/(?P<id>\d+)$', views.viewAuthor),
    url(r'^removeAuthor/(?P<id>\d+)$', views.removeAuthor),
]
