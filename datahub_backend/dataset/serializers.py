from .models import Dataset, Tag
from rest_framework import serializers


class DatasetSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Dataset
        fields = '__all__'

    def get_file(self, obj):
        return obj.get_file_url()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
