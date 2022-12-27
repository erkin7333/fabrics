from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """User model."""
    phone = models.CharField(max_length=20, blank=True, null=True)
    men = models.BooleanField(default=False)
    women = models.BooleanField(default=False)

    def __str__(self):
        return self.username