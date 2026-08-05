from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



def home(request):
    return render(request,"home.html")

def test_email(request):

    send_mail(
        subject='Test Email',
        message='Hello Rajvi, This is Django Test Email.',
        from_email=None,
        recipient_list=['rajvigandhi05@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse("Email Sent Successfully")



def send_password_reset_email(request):

    user_email = ""

    reset_link = "http://127.0.0.1:8000/reset-password/"

    subject = "Reset Your Password"

    message = f"""
Hello,

We received a request to reset your password.

Click the link below to create a new password.

{reset_link}

If you didn't request this change, simply ignore this email.

Regards,
Customer Support
"""

    send_mail(
        subject,
        message,
        None,
        [user_email],
        fail_silently=False,
    )

    return HttpResponse("Password Reset Email Sent Successfully")

    user_email = ""

    reset_link = "http://127.0.0.1:8000/reset-password/"

    subject = "Reset Your Password"

    message = f"""
Hello,

We received a request to reset your password.

Click the link below to create a new password.

{reset_link}

If you didn't request this change, simply ignore this email.

Regards,
Customer Support
"""

    send_mail(
        subject,
        message,
        None,
        [user_email],
        fail_silently=False,
    )

    return HttpResponse("Password Reset Email Sent")


#task=3
# def order_email(request):

#     html_content = render_to_string(
#         "order_confirmation.html"
#     )

#     email = EmailMultiAlternatives(

#         subject="Order Confirmed 🍔",

#         body="Order Confirmed",

#         to=[""]

#     )

#     email.attach_alternative(html_content, "text/html")

#     email.send()

#     return HttpResponse("HTML Email Sent")

#ask-4
def order_email(request):

    context = {
        "name": "Rajvi",

        "items": [
            {"name": "Veg Burger", "qty": 2},
            {"name": "Pizza", "qty": 1},
            {"name": "Cold Drink", "qty": 3},
        ],

        "total": 850,
    }

    html_content = render_to_string(
        "order_confirmation.html",
        context
    )

    email = EmailMultiAlternatives(
        subject="Order Confirmed 🍔",
        body="Order Confirmed",
        to=[""]   # અહીં તમારું actual Gmail લખો
    )

    email.attach_alternative(html_content, "text/html")

    email.send()

    return HttpResponse("Dynamic HTML Email Sent Successfully")

def welcome_email(request):

    context = {
        "name": "Rajvi"
    }

    html_content = render_to_string(
        "welcome_email.html",
        context
    )

    email = EmailMultiAlternatives(
        subject="🏏 Welcome to IPL Fantasy League – Build Your Dream Team!",
        body="Welcome to IPL Fantasy League",
        to=[""]   # અહીં તમારું actual Gmail લખો
    )

    email.attach_alternative(html_content, "text/html")

    email.send()

    return HttpResponse("Welcome Email Sent Successfully")