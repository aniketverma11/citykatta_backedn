from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from datahub_backend.dataset.models import Dataset, Tag, Category, SubCategory
from datahub_backend.dataset.serializers import (
    DatasetSerializer,
    TagSerializer,
    CategorySerializer,
    SubCategorySerializer,
    CategoryListSerializer,
)


class DatasetViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get("category_id")
        if category_id:
            return self.queryset.filter(category_id=category_id)
        return self.queryset.filter()


class PopularCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        top = self.request.query_params.get("top", "7")
        if top:
            return self.queryset.all()[:int(top)]
