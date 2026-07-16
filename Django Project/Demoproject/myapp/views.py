from django.shortcuts import render
import random
# Create your views here.
counter=0
def index(request):
  name='ashok'
  num=random.randint(1111,99999)
  global counter
  counter+=1
  return render(request,'index.html',{'nm':name,'num':num,'count':counter,'students': ['John', 'Emma', 'David', 'Sophia']})
