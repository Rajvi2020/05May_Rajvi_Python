from django import forms
class AddRestaurantForm(forms.Form):
  restaurant_name=forms.CharField(min_length=3,max_length=100,
  label="Restaturant_name")
  cuisine_type=forms.CharField(max_length=50, label="cusine type")
  contact_email=forms.EmailField(max_length=50,label="email")

