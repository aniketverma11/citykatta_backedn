from django.shortcuts import render
from rest_framework import viewsets

from datahub_backend.provider.models import Review, ProviderModel
from datahub_backend.provider.serializers import ReviewSerializer, ProviderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderSerializer
