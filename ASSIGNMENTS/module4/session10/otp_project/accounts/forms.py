from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

class OTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        label="OTP",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter 6-digit OTP"
        })
    )