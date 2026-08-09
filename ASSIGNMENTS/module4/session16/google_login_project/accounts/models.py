from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class OTPVerification(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        time_difference = timezone.now() - self.created_at
        return time_difference.total_seconds() > 300

    def __str__(self):
        return self.phone_number