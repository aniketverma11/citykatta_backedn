from rest_framework import viewsets, generics

from . import models
from datahub_backend.dataset import serializers


class GlobalSearchListAPIView(generics.ListAPIView):
    queryset = None
    serializer_class = None
    pagination_class = None


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryListSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get("category_id")
        if category_id:
            return self.queryset.filter(category_id=category_id)
        return self.queryset.filter()


class PopularCategoryAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        top = self.request.query_params.get("top", "7")
        if top:
            return self.queryset.all()[: int(top)]


class UseCaseListAPIView(generics.ListAPIView):
    queryset = models.UseCase.objects.all()
    serializer_class = serializers.UseCaseSerializer
