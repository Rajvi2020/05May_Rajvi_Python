import re

#mystr="That isthis Python!"  #here error
mystr="this is python" #this will give match object 
x=re.match("this",mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")

# This function determines if the RE matches at the beginning of the string.

'''Return Type:

Match Object

જો match ન મળે:

None'''