from django.db import models

# Create your models here.
class studentinfo(models.Model):
  GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  email=models.EmailField()
  mobile=models.BigIntegerField()
  gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
  dob=models.DateField()
  course=models.CharField(max_length=20)
  city=models.CharField(max_length=20)
  address=models.TextField()
  # def __str__(self):
  #   return self.last_name
  


