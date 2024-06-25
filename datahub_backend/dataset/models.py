from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey('provider.ProviderModel', on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='datasets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_format = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

