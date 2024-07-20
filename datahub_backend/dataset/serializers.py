from .models import Dataset, Tag, SubCategory, Category, UseCase
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("is_active", "is_deleted")


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        exclude = ("is_active", "is_deleted")


class CategoryListSerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ("is_active", "is_deleted")

    def get_sub_category(self, obj):
        return SubCategorySerializer(
            SubCategory.objects.filter(category=obj), many=True
        ).data


class DatasetROSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    sub_category = SubCategorySerializer(read_only=True)
    use_cases = serializers.SerializerMethodField()

    class Meta:
        model = Dataset
        fields = "__all__"

    def get_file(self, obj):
        return obj.get_file_url()

    def get_use_cases(self, obj):
        return obj.use_cases.split(",")


class DatasetWOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = "__all__"
