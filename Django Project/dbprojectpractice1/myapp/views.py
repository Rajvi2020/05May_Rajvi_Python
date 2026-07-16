from django.shortcuts import render,redirect
from .forms import *
from .models import *


def index(request):
  if request.method=='POST':
    
    student=studentform(request.POST)
    if student.is_valid():
      student.save
      print("record inserted sucessfully.")
    else:
      print(student.errors)


  return render(request,'index.html')

def showdata(request):
  students=studentinfo.objects.all()
  return render(request,'showdata.html',{'students':students})

def updatedata(request,id):
  stid=studentinfo.objects.get(id=id)
  if request.method=='POST':
    student=studentform(request.POST,instance=stid)
    if student.is_valid():
      student.save()
      print("record updated succesfully")
      return redirect('showdata')
    else:
      print(student.errors)
  return render(request,'updatedata.html',{'stid':stid})


def deletedata(request,id):
  stid=studentinfo.objects.get(id=id)
  studentinfo.delete(stid)
  return redirect('showdata')