from django import forms
from .models import *
class userform(forms.ModelForm):
  class Meta:
    model=Userinfo
    fields="__all__"
    
