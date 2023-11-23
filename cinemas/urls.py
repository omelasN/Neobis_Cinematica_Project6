from django.urls import path
from .views import *


urlpatterns = [
    path('cinema-admin/', CinemaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('room-admin/', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cinema/', CinemaUserView.as_view(), name="cinema"),
    path('room/', RoomUserView.as_view(), name="room"),
]
