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


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"