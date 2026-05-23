sub1=int(input("enter the sub1 marks"))
sub2=int(input("enter the sub2 marks"))
sub3=int(input("enter the sub3 marks"))
sub4=int(input("enter the sub4 marks"))
total=sub1+sub2+sub3+sub4 
print("total is ",total)
per=total*100/400 
if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 :
 if per>=70:
  print("A+ grader and per is",per)
 elif per>=60:
  print("a grade and per is",per)
 elif per>=40:
  print("b grade and per is",per) 
else:
  print("fail")      