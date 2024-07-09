from django.db import models

from datahub_backend.core.storages import generate_presigned_url
from datahub_backend.core.utils import unique_filename


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey('provider.ProviderModel', on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='datasets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_format = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=unique_filename, blank=True, null=True)

    def get_file_url(self):
        if self.file:
            return generate_presigned_url(self.file)
        return ""


class Tag(models.Model):
    name = models.CharField(max_length=50)

