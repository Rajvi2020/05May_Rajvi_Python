import re
username=input('enter name')
#unm_pattern="[A-Z]+[a-z]+[0-9]"  #when a-z capital and small is compusaloy 
#when not compuslory write like this
unm_pattern="[A-Za-z0-9]"
x=re.findall(unm_pattern,username)
if x:
  print("username is valid")
else:
  print("error!")  