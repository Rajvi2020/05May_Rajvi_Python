# myset=set()
# num=int(input("enter the no of elemets of set"))
# for i in range(num):
#   ele=input("enter the element")
#   myset.add(ele)
# print(myset)  

myset={'a','b','c','d','e','a','b'}
#print(len(myset))

if 'B' in myset:
  print("yes")
else:
  print("no")

#myset.clear()
#print(myset)
#print(myset[0]) we can not do this because set is unordered.

myset.add('f')
#print(myset)

myset.update(['g','q','r'])
#print(myset)
#diff between set update and add method is that update can add multiple elements while add can only one.

myset.remove('f')
#print(myset)
#myset.pop()
#print(myset)
#clear=removes all element
#pop=remove random ele
#remove=remove specific element

newset={'1','2','3'}
print(newset)
#x=myset.union(newset)
#print(x)
x=myset.intersection(newset)
print(myset)