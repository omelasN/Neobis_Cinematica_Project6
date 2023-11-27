from rest_framework import serializers
from .models import *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class SeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class ShowTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = "__all__"


class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

