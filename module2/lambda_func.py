x=lambda a,b:a+b
print(x(12,13))

def getsum():
  print("sum",x(12,45))
getsum()

#lambda x,y,a,b:x*y ,a+b we can not do the two operation at once.\
q=lambda x,y,a,b:a+b*x+y
print(q(1,2,3,4))