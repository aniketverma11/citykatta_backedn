from django.urls import path

from datahub_backend.core import views

app_name = "core"


urlpatterns = [
    path("countries", views.CountryListAPIView.as_view(), name="countries"),
    path("data-request", views.DataRequestCreateAPIView.as_view(), name="data-request"),
    path("contact", views.ContactUsCreateAPIView.as_view(), name="contact-create-view"),
]
