from django import forms
from .models import *
class employeeform(forms.ModelForm):
  class Meta:
    model=Employee
    fields='__all__'