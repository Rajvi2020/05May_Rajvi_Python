

# Create your views here.
import random

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ForgotPasswordForm, OTPForm


def forgot_password_view(request):

    if request.method == "POST":

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]

            otp = random.randint(100000, 999999)

            request.session["otp"] = str(otp)
            request.session["email"] = email

            request.session.set_expiry(300)

            send_mail(
                subject="Password Reset OTP",
                message=f"Your OTP is {otp}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, "OTP sent successfully!")

            return redirect("verify_otp")

    else:
        form = ForgotPasswordForm()

    return render(request, "forgot_password.html", {"form": form})
def verify_otp_view(request):

    if request.method == "POST":

        form = OTPForm(request.POST)

        if form.is_valid():

            entered_otp = form.cleaned_data["otp"]

            session_otp = request.session.get("otp")

            if entered_otp == session_otp:

                messages.success(request, "OTP Verified Successfully!")

                request.session.pop("otp", None)

                return redirect("forgot_password")

            else:

                messages.error(request, "Invalid OTP")

    else:

        form = OTPForm()

    return render(request, "verify_otp.html", {"form": form})