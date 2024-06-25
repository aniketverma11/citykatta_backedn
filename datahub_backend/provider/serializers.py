from rest_framework import serializers

from datahub_backend.provider.models import Review, ProviderModel


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'
