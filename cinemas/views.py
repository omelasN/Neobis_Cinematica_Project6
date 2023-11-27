from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializers
    permission_classes = [IsAdminUser]


class CinemaUserView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializers
    permission_classes = [AllowAny]


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializers
    permission_classes = [IsAdminUser]


class SeatUserView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializers
    permission_classes = [AllowAny]


class ShowTimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializers
    permission_classes = [IsAdminUser]


class ShowTimeUserView(generics.ListCreateAPIView):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializers
    permission_classes = [AllowAny]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [IsAdminUser]


class RoomUserView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [AllowAny]


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializers
    permission_classes = [IsAdminUser]


class DiscountUserView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializers
    permission_classes = [AllowAny]


class TicketUserView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers
    permission_classes = [AllowAny]