from django import forms
from .models import *
class studentform(forms.ModelForm):
  class Meta:
    model=studentinfo
    fields='__all__'
    