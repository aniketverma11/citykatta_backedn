from django.db import models
from model_utils.models import TimeStampedModel

from datahub_backend.utils.behaviours import StatusMixin


class Country(StatusMixin, TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class DataRequest(TimeStampedModel):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(
        "dataset.Category", related_name="request_category"
    )
    geography = models.ManyToManyField("core.Country", related_name="request_country")
    budget = models.CharField(max_length=10)
    detail = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
