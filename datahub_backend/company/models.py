from django.db import models

from datahub_backend.core.models import Country


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    headquater = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.company + " " + self.question
