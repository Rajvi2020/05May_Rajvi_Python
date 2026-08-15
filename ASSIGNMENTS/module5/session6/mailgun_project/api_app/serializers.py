from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        help_text="Recipient's email address"
    )
    subject = serializers.CharField(
        required=False,
        default="Welcome to Our Platform!",
        help_text="Email subject line"
    )
    message = serializers.CharField(
        required=False,
        default="Welcome to our platform! We are excited to have you on board.",
        help_text="Email body text"
    )


class SendSMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,
        help_text="Recipient's phone number in E.164 format (e.g. +1234567890)"
    )
    message = serializers.CharField(
        required=True,
        help_text="SMS content message"
    )


class PaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="Payment amount in cents (e.g. 1000 for $10.00)"
    )
    currency = serializers.CharField(
        required=False,
        default="usd",
        max_length=10,
        help_text="3-letter ISO currency code (e.g., usd, eur, inr)"
    )
    description = serializers.CharField(
        required=False,
        default="API Test Payment Simulation",
        help_text="Description of the purchase"
    )


class GoogleLoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text="Google OAuth2 ID Token received from Google Sign-In frontend"
    )
    access_token = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text="Google OAuth2 Access Token"
    )
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        help_text="Optional user email for testing/simulation flow"
    )
    first_name = serializers.CharField(
        required=False,
        allow_blank=True,
        default="Google"
    )
    last_name = serializers.CharField(
        required=False,
        allow_blank=True,
        default="User"
    )

    def validate(self, attrs):
        id_token = attrs.get('id_token')
        access_token = attrs.get('access_token')
        email = attrs.get('email')

        if not id_token and not access_token and not email:
            raise serializers.ValidationError(
                "Either 'id_token', 'access_token', or 'email' must be provided for Google Login authentication."
            )
        return attrs
