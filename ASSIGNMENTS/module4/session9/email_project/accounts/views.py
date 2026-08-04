from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core.mail import send_mail

from django.conf import settings

def test_email(request):

    send_mail(

        subject="Testing Email",

        message="Hello! This email is sent from Django.",

        from_email=settings.EMAIL_HOST_USER,

        recipient_list=["receiver@gmail.com"],

        fail_silently=False

    )

    return HttpResponse("Email Sent Successfully")