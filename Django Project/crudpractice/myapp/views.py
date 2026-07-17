from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def welcome(request):
  return render(request,'welcome.html')

def add(request):
  name = request.GET.get("name", "")
  if request.method=='POST':
    user=userform(request.POST)
    if user.is_valid():
      user.save()
      print("record inserted")
      return redirect('showdata')
    else:
      print(user.errors)
  else:
    user=userform(initial={'name':name})
  return render(request,'add.html',{'user':user,'name':name})

def showdata(request):
  data=User.objects.all()
  return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
  stid=User.objects.get(id=id)
  if request.method=='POST':
    user=userform(request.POST,instance=stid)
    if user.is_valid():
      user.save()
      print("record updated")
      return redirect('showdata')
    else:
      print('user.errors')
  else:
    user=userform(instance=stid)
  return render(request,'updatedata.html',{'stid':stid})


def deletedata(request,id):
  stid=User.objects.get(id=id)
  User.delete(stid)
  return redirect('showdata')




