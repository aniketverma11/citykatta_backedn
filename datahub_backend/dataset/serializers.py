from .models import Dataset, Tag, SubCategory, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = "__all__"


class DatasetSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    sub_category = SubCategorySerializer(read_only=True)

    class Meta:
        model = Dataset
        fields = "__all__"

    def get_file(self, obj):
        return obj.get_file_url()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
