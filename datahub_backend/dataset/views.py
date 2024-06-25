from django.shortcuts import render
from rest_framework import viewsets

from datahub_backend.dataset.models import Dataset, Tag
from datahub_backend.dataset.serializers import DatasetSerializer, TagSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
