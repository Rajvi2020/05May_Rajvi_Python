from django.db import models

# Create your models here.
class userinfo(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField()
  mobile=models.BigIntegerField()
  city=models.CharField(max_length=20)
  # def __str__(self):
  #   return self.name