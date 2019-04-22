#---------------------------------------------------
# HandyHelper urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.user_login),
    url(r'^user/create$', views.user_create),
    url(r'^task/new$', views.task_new),
    url(r'^task/(?P<id>\d+)/edit$', views.task_edit),
    url(r'^task/(?P<id>\d+)/update$', views.task_update),
    url(r'^task/(?P<id>\d+)/destroy$', views.task_delete),
    url(r'^task/(?P<id>\d+)/view$', views.task_view),
    url(r'^task/(?P<id>\d+)/add_to_list$', views.add_to_list),
    url(r'^task/(?P<id>\d+)/remove_from_list$', views.delete_from_list),
    url(r'^task/(?P<id>\d+)/give_up$', views.give_up),
    url(r'^user/create$', views.user_create),
    url(r'^task/create$', views.task_create),
    url(r'^dashboard$', views.task_read),
    url(r'^logout$', views.user_logout),
]
