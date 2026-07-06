from django.db import models
from django.auth.contrib.models impot AbstractUser
# Create your models here.

class ActivitySerializer(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

class CustomUser(AbstractUser):
    email = models.EmailField()
    age = IntegerField()

