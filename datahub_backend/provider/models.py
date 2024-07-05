from django.db import models


class ProviderModel(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    privacy_policy = models.CharField(max_length=100)

    def __str__(self):
        return self.owner


class Review(models.Model):
    dataset = models.ForeignKey(ProviderModel, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(0, 0), (1,1), (2,2), (3,3), (4,4), (5, 5)], default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
