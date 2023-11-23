from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinemas.objects.all()
    serializer_class = CinemaSerializers
    permission_classes = [IsAdminUser]


class CinemaUserView(generics.ListCreateAPIView):
    queryset = Cinemas.objects.all()
    serializer_class = CinemaSerializers
    permission_classes = [AllowAny]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Cinemas.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [IsAdminUser]


class RoomUserView(generics.ListCreateAPIView):
    queryset = Cinemas.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [AllowAny]


