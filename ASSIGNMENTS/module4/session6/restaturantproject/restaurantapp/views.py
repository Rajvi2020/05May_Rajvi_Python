from django.shortcuts import render
from .forms import  *
# Create your views here.
def restaurant(request):
  
  if request.method=="POST":
    form=AddRestaurantForm(request.POST)
    if form.is_valid():
      data={
      "restaurant_name":form.cleaned_data['restaurant_name'],
      "cuisine_type": form.cleaned_data["cuisine_type"],
                "contact_email": form.cleaned_data["contact_email"],

              }
      return render(request,'sucess.html',data)
  else:
    form=AddRestaurantForm()
    return render(request,"restaurant.html",{'form':form})