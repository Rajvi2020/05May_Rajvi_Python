from django.db import models

# Create your models here.


class Employee(models.Model):

    # Gender Choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Employee Details
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()

    # Job Details
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    # Address Details
    city = models.CharField(max_length=30)
    address = models.TextField()
    # def __str__(self):
    #     return self.city

  