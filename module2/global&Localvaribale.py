a=65
b=48
def production():
  print(a*b)

production()

#this will give error
# x=10
# print(x)
# def getvalue():
#   x+=10
#   print(x)
# getvalue()



x=10
print(x)
def getvalue():
    #x=50
    global x
    x+=10
    print(x)
getvalue()
print(x)
