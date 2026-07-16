from django import forms
from .models import *
class Restaurantform(forms.ModelForm):

    name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Restaurant Name'
        }),
        error_messages={
            'min_length': 'Restaurant name must be at least 3 characters.'
        }
    )

    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(),
        error_messages={
            'min_value': 'Rating must be between 1 and 5.',
            'max_value': 'Rating must be between 1 and 5.'
        }
    )

    class Meta:
        model = Restaurant
        fields = '__all__'