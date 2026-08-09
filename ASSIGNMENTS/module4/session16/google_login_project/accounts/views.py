import random
import requests

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from twilio.rest import Client

from .forms import RegistrationForm
from .models import OTPVerification


# =========================================================
# HOME
# =========================================================

def home(request):

    return render(request, "home.html")


# =========================================================
# REGISTER + MAILGUN WELCOME EMAIL
# =========================================================

def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            username = user.username
            email = user.email

            # ---------------------------------------------
            # Mailgun API
            # ---------------------------------------------

            mailgun_url = (
                f"https://api.mailgun.net/v3/"
                f"{settings.MAILGUN_DOMAIN}/messages"
            )

            data = {
                "from": f"Django App <mailgun@{settings.MAILGUN_DOMAIN}>",

                "to": [email],

                "subject": "Welcome to Django App!",

                "text": (
                    f"Hello {username},\n\n"
                    "Welcome to our website!\n"
                    "Thank you for registering."
                ),
            }

            try:

                response = requests.post(
                    mailgun_url,
                    auth=(
                        "api",
                        settings.MAILGUN_API_KEY
                    ),
                    data=data,
                )

                if response.status_code == 200:

                    messages.success(
                        request,
                        "Registration successful! "
                        "Welcome email sent."
                    )

                else:

                    messages.warning(
                        request,
                        "Registration successful, "
                        "but email could not be sent."
                    )

            except Exception:

                messages.warning(
                    request,
                    "Registration successful, "
                    "but email could not be sent."
                )

            # ---------------------------------------------
            # Registration Success Page
            # ---------------------------------------------

            return render(
                request,
                "registration_success.html",
                {
                    "username": username,
                    "email": email,
                }
            )

    else:

        form = RegistrationForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


# =========================================================
# SEND OTP
# =========================================================

def send_otp(request):

    if request.method == "POST":

        phone_number = request.POST.get("phone_number")

        # Generate 6-digit OTP
        otp = str(
            random.randint(100000, 999999)
        )

        # ---------------------------------------------
        # Save OTP in database
        # ---------------------------------------------

        OTPVerification.objects.create(
            phone_number=phone_number,
            otp=otp
        )

        # ---------------------------------------------
        # Twilio
        # ---------------------------------------------

        try:

            client = Client(
                settings.TWILIO_ACCOUNT_SID,
                settings.TWILIO_AUTH_TOKEN
            )

            client.messages.create(
                body=(
                    f"Your OTP is {otp}. "
                    "Do not share it with anyone."
                ),

                from_=settings.TWILIO_PHONE_NUMBER,

                to=phone_number
            )

            messages.success(
                request,
                "OTP sent successfully!"
            )

        except Exception as e:

            messages.error(
                request,
                "OTP could not be sent."
            )

        return render(
            request,
            "send_otp.html"
        )

    return render(
        request,
        "send_otp.html"
    )


# =========================================================
# VERIFY OTP
# =========================================================

def verify_otp(request):

    if request.method == "POST":

        phone_number = request.POST.get(
            "phone_number"
        )

        entered_otp = request.POST.get(
            "otp"
        )

        # Get latest OTP for this phone number
        otp_record = (
            OTPVerification.objects
            .filter(
                phone_number=phone_number,
                is_verified=False
            )
            .order_by("-created_at")
            .first()
        )

        # ---------------------------------------------
        # OTP record does not exist
        # ---------------------------------------------

        if not otp_record:

            messages.error(
                request,
                "Invalid OTP."
            )

            return render(
                request,
                "verify_otp.html"
            )

        # ---------------------------------------------
        # Check OTP expiry
        # ---------------------------------------------

        if otp_record.is_expired():

            messages.error(
                request,
                "OTP has expired. Please request a new OTP."
            )

            return render(
                request,
                "verify_otp.html"
            )

        # ---------------------------------------------
        # Check OTP
        # ---------------------------------------------

        if otp_record.otp == entered_otp:

            otp_record.is_verified = True

            otp_record.save()

            messages.success(
                request,
                "OTP verified successfully!"
            )

            return render(
                request,
                "verify_otp.html"
            )

        else:

            messages.error(
                request,
                "Invalid OTP. Please try again."
            )

    return render(
        request,
        "verify_otp.html"
    )