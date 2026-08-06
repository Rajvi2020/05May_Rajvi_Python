from django.db import models
from django.contrib.auth.models import User


# Zomato like My Orders
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product_name = models.CharField(
        max_length=100
    )
    price = models.IntegerField()


    def __str__(self):
        return self.product_name



# Flipkart like Product
class Product(models.Model):
    name = models.CharField(
        max_length=100
    )
    price = models.IntegerField()


    def __str__(self):
        return self.name



# BookMyShow like Movie Review
class Review(models.Model):
    movie = models.CharField(
        max_length=100
    )
    review = models.TextField()


    def __str__(self):
        return self.movie



# Spotify like Playlist
class Playlist(models.Model):
    name = models.CharField(
        max_length=100
    )


    def __str__(self):
        return self.name