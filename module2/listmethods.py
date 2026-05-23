l=[1,2,4,6,15,25]
# print(l)
# print(l[0])
# print(l[-1])
# print(l[1:4])
# print(len(l))
# for i in l:
#   print(i)

if 8 in l:
  print("yes...")
else:
  print("sorry  ")  

l[1]=40
print(l)

l.append(4)
print(l)

l.insert(4,100)
print(l)

l.remove(100)
print(l)

l.pop()
print(l)

l.pop(0)
print(l)

del l[0]
print(l)

#l.clear()
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l1=[5,7,9,2,4]
print(l+l1)

l.extend(l1)
print(l)

l2=l.copy()
print(l2)


