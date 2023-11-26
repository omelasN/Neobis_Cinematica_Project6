from rest_framework import serializers
from .models import *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinemas
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"


class SeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = "__all__"


class ShowTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowTimes
        fields = "__all__"

