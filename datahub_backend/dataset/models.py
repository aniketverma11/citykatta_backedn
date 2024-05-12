from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey('dataset.provider', on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='datasets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_format = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Review(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(0, 0), (1,1), (2,2), (3,3), (4,4), (5, 5)], default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Provider(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.TextField()
    contact_email = models.EmailField()
    website = models.URLField()
