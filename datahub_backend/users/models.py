from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from datahub_backend.dataset.models import Dataset


class User(AbstractUser):
    """
    Default custom user model for DataHub Backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    USER_TYPE_CHOICES = [('admin', 'Admin'), ('vendor', 'Vendor'), ('user', 'User')]
    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    user_type = models.CharField(_("User Type"), blank=True, max_length=255, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Favorite(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
