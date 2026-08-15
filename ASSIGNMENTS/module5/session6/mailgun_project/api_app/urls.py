from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    SendEmailView,
    SendSMSView,
    StripePaymentView,
    GoogleLoginView
)

urlpatterns = [
    # Task 1: Mailgun Welcome Email Endpoint
    path('send-email/', SendEmailView.as_view(), name='send-email'),

    # Task 2: Twilio SMS Endpoint
    path('send-sms/', SendSMSView.as_view(), name='send-sms'),

    # Task 3: Stripe Payment Simulation Endpoint
    path('pay/', StripePaymentView.as_view(), name='pay'),

    # Task 4: Google Login & JWT Authentication Endpoint
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),

    # Token refresh utility for SimpleJWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
