from django.urls import include, path

from rest_framework import routers

from datahub_backend.dataset import views

router = routers.DefaultRouter()

router.register(r"datasets", views.DatasetViewSet)
router.register(r"tags", views.TagViewSet)


urlpatterns = [
    path("category", views.CategoryListAPIView.as_view(), name="category"),
    path("sub-category", views.SubCategoryListAPIView.as_view(), name="sub-category"),
    path("dataset/", include(router.urls)),
]
