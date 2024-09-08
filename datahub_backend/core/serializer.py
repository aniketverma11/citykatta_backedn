from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from datahub_backend.core.models import Country, DataRequest, ContactUs

User = get_user_model()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DataRequestSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = DataRequest
        exclude = ["user"]

    def create(self, validated_data):
        if self.request.user:
            username = validated_data.pop("username")
            password = validated_data.pop("password")
            user = User.objects.create_user(username=username, password=password)
        else:
            user = self.request.user
        data_request = DataRequest.objects.create(user=user, **validated_data)
        category = validated_data.pop("category")
        geography = validated_data.pop("geography")
        data_request.category.set(category)
        data_request.geography.set(geography)
        return data_request

    def validate(self, data):
        user = data.get("username")
        if not user:
            return
        user_object = User.objects.get(username=user)
        if user_object:
            raise ValidationError({"data": "User is already registered."})


class ContactUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
