from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import *


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes = [IsAdminUser]


class MovieUserView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes = [IsAuthenticated]


class MovieCategoryViewSet(viewsets.ModelViewSet):
    queryset = MovieCategory.objects.all()
    serializer_class = MovieCategorySerializers
    permission_classes = [IsAdminUser]


class MovieCategoryUserView(generics.ListAPIView):
    queryset = MovieCategory.objects.all()
    serializer_class = MovieCategorySerializers
    permission_classes = [IsAuthenticated]

