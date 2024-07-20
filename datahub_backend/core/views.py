from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializer


class CountryListAPIView(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializer.CountrySerializer


class DataRequestCreateAPIView(generics.CreateAPIView):
    queryset = models.DataRequest.objects.all()
    serializer_class = serializer.DataRequestSerializer
