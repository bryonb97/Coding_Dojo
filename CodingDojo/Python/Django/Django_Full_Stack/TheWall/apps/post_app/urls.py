#---------------------------------------------------
# post_app urls.py 
#---------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_post$', views.createPost),
    url(r'^success$', views.success),
    url(r'^post/delete/(?P<id>\d+)$', views.delete_post),
    url(r'^add_comment$', views.comment),
    url(r'^logout$', views.logout),
]
