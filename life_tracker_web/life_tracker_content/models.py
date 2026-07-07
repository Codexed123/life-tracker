from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ActivitySerializer(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

class CustomUser(AbstractUser):
    email = models.EmailField()
