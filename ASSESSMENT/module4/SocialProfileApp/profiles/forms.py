from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'age',
            'bio',
            'city',
            'is_public',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email'
            }),

            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter your age'
            }),

            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell something about yourself'
            }),

            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city'
            }),
        }