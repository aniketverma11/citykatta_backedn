from django.shortcuts import render
from rest_framework import viewsets

from datahub_backend.dataset.models import Dataset, Tag
from datahub_backend.dataset.serializers import (
    DatasetROSerializer,
    DatasetWOSerializer,
    TagSerializer,
)


class DatasetViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Dataset.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DatasetROSerializer
        return DatasetWOSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
