from django.db import models

# Create your models here.
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title    