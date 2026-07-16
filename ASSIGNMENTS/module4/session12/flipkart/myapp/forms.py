from django import forms
from .models import *
class productform(forms.ModelForm):
  class Meta:
    model=product
    fields='__all__'
    

