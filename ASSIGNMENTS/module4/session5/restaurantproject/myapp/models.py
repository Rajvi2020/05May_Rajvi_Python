from django.db import models

# Create your models here.
class Restaturant(models.Model):
  name=models.CharField(max_length=20)
  cuisine=models.CharField(max_length=20)
  rating=models.FloatField()
  def __str__(self):
    return self.name