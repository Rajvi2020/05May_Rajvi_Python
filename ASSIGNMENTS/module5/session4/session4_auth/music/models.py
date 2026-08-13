from django.db import models




class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.food_name

class Cart(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_name