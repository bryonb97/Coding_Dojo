#---------------------------------------------------
# quote_app urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^quote$', views.quote_read),
    url(r'^quote/(?P<id>\d+)/edit$', views.quote_edit),
    url(r'^quote/(?P<id>\d+)/update$', views.quote_update),
    url(r'^quote/(?P<id>\d+)/destroy$', views.quote_delete),
    url(r'^quote/create$', views.quote_create),
    url(r'^user/(?P<id>\d+)$', views.user_read),
    url(r'^user/(?P<id>\d+)/update$', views.user_update),
    url(r'^destroy/(?P<id>\d+)$', views.user_delete),
    url(r'^user/create$', views.user_create),
    url(r'^login$', views.user_login),
    url(r'^logout$', views.logout),
    url(r'^quote/(?P<id>\d+)/like$', views.like_quote),
    url(r'^admin$', views.admin_tools),
]
