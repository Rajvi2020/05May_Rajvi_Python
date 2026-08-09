from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name