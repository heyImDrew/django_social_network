from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth = models.DateField(null=True, blank=True)