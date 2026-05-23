"""n=int(input("enter the no for which you want to print table"))
i=1
while i<=10:
  print(n,"*",i,"=",n*i)
  i+=1"""

n=int(input("enter the no for which you want to print table"))
for i in range(1,11):
   #print(f"{n} * {i} = {n*i}")
   print("{} * {} = {}".format(n,i,n*i))