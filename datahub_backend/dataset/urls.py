from django.urls import include, path

from rest_framework import routers

from datahub_backend.dataset import viewset
from datahub_backend.dataset import views

router = routers.DefaultRouter()

router.register(r"datasets", viewset.DatasetViewSet)
router.register(r"tags", viewset.TagViewSet)


urlpatterns = [
    path("category", views.CategoryListAPIView.as_view(), name="category"),
    path("sub-category", views.SubCategoryListAPIView.as_view(), name="sub-category"),
    path("top-category", views.PopularCategoryAPIView.as_view(), name="top-category"),
    path(
        "global-search", views.GlobalSearchListAPIView.as_view(), name="global-search"
    ),
    path("use-cases", views.UseCaseListAPIView.as_view(), name="use-cases"),
    path("", include(router.urls)),
]
