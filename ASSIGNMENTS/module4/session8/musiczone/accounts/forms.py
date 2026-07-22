from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'w-full border rounded-lg px-3 py-2',
            'placeholder':'Enter username'
        })
    )


    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'w-full border rounded-lg px-3 py-2',
            'placeholder':'Enter email'
        })
    )


    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'w-full border rounded-lg px-3 py-2',
            'placeholder':'Enter password'
        })
    )


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]