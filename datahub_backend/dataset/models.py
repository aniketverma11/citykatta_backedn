from django.db import models

from datahub_backend.core.storages import generate_presigned_url
from datahub_backend.core.utils import unique_filename
from datahub_backend.utils.behaviours import StatusMixin


class Category(StatusMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UseCase(StatusMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class SubCategory(StatusMixin):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        "dataset.Category",
        on_delete=models.CASCADE,
        related_name="subcategories",
        related_query_name="subcategories",
    )

    def __str__(self):
        return self.name


class Dataset(StatusMixin):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey("provider.ProviderModel", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        "dataset.SubCategory", on_delete=models.DO_NOTHING, null=True
    )
    description = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="datasets")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    use_cases = models.CharField(max_length=255, null=True)
    file_format = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=unique_filename, blank=True, null=True)

    def get_file_url(self):
        if self.file:
            return generate_presigned_url(self.file)
        return ""


class Tag(models.Model):
    name = models.CharField(max_length=50)
