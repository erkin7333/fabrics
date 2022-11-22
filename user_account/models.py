from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    men = models.BooleanField(default=False)
    women = models.BooleanField(default=False)

    def __str__(self):
        return self.username