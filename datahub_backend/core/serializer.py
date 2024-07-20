from rest_framework import serializers

from datahub_backend.core.models import Country, DataRequest


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DataRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRequest
        fields = "__all__"
