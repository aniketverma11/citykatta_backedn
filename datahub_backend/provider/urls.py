from django.urls import include, path

from rest_framework import routers

from datahub_backend.provider import views

router = routers.DefaultRouter()

router.register(r"reviews", views.ReviewViewSet)
router.register(r"providers", views.ProviderViewSet)
