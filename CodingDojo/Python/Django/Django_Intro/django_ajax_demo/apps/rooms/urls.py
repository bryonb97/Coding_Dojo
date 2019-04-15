# ---------------------------------------------------
# rooms urls.py
# ---------------------------------------------------
from django.conf import settings
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^rooms$', TemplateView.as_view(
        template_name="rooms/main.html"), name='room_main'),
    url(r'^rooms/list$', views.RoomList.as_view(), name='room_list'),
    url(r'rooms/create$', views.RoomCreate.as_view(), name='room_create'),
    url(r'^rooms/update/<int:pk>$', views.RoomUpdate.as_view(), name='room_update'),
    url(r'^rooms/delete/<int:pk>$', views.RoomDelete.as_view(), name='room_delete'),
    url(r'^rooms/<int:pk>$', views.RoomDetail.as_view(), name='room_detail'),
]
