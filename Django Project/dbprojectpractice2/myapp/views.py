from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
  if request.method=="POST":
    empl=employeeform(request.POST)
    if empl.is_valid():
      empl.save()
      print("record inserted")
    else:
      print(empl.errors)  

  return render(request,'index.html')

def showdata(request):
  emplo=Employee.objects.all()
  return render(request,'showdata.html',{'emplo':emplo})


def updatedata(request,id):
  stid=Employee.objects.get(id=id)
  if request.method=='POST':
    empl=employeeform(request.POST,instance=stid)
    if empl.is_valid():
      empl.save()
      print("record updated sucessfully")
      return redirect('showdata')
    else:
      print(empl.errors)
  return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
  stid=Employee.objects.get(id=id)
  Employee.delete(stid)
  return redirect('showdata')