from django.shortcuts import render
from rest_framework import viewsets

from datahub_backend.dataset.models import Dataset, Tag, Review, Provider
from datahub_backend.dataset.serializers import DatasetSerializer, TagSerializer, ReviewSerializer, ProviderSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
