from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
  if request.method=="POST":
    products=productform(request.POST)
    if products.is_valid():
      products.save()
      print("record inserted sucessfully")
    else:
      print(products.errors)  
  return render(request,'index.html')

def showdata(request):
  data=product.objects.all()
  return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
  pid=product.objects.get(id=id)
  if request.method=='POST':
    products=productform(request.POST,instance=pid)
    if products.is_valid():
      products.save()
      print("record updated")
      return redirect('showdata')
    else:
      print(products.errors)
    

 
  return render(request,'updatedata.html',{'pid':pid})

def deletedata(request,id):
  pid=product.objects.get(id=id)
  pid.delete()
  return redirect('showdata')
