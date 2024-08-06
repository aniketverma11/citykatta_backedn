from django.shortcuts import render
from rest_framework import generics, permissions

from . import models
from . import serializer


class CountryListAPIView(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializer.CountrySerializer


class DataRequestCreateAPIView(generics.CreateAPIView):
    queryset = models.DataRequest.objects.all()
    serializer_class = serializer.DataRequestSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
