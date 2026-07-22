from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
# Create your views here.
#signup
def signup(request):
  if request.method=='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      user=form.save(commit=False)
      user.set_password(form.cleaned_data['password'])
      user.save()
      return redirect('login')
  else:
      form=SignupForm()
  return render(request,'signup.html',{'form':form})

#login
def user_login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user:
      login(request,user)
      return redirect('welcome')
  return render(request,'login.html')

#logout
def user_logout(request):
  logout(request)
  return redirect('home')

#welcome
@login_required
def welcome(request):
  return render(request,'welcome.html')

#home
def home(request):
  return render(request,'home.html')    