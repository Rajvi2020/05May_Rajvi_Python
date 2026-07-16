from django.shortcuts import render
from .forms import *
# Create your views here.


def index(request):
  if request.method=='POST':
    restaurant=Restaurantform(request.POST)
    if restaurant.is_valid():
      restaurant.save()
      print("record inserted")
      restaurant=Restaurantform()
    else:
      print(restaurant.errors)
  else:    
   restaurant=Restaurantform()
  return render(request,'index.html',{'restaurant':restaurant})