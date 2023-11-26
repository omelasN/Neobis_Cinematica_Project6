from rest_framework import serializers
from .models import *


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'
