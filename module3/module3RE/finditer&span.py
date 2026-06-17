'''finditer() અને span() બંને કેમ વાપર્યા?

કારણ કે finditer() Match Object આપે છે, અને span() એ Match Object માંથી position કાઢે છે.'''

# use of finditer

import re
name="Python is world's best programming language "
for i in re.finditer("world's",name):
  ans=i.span()
  print(ans)


  '''if we want to use without loop 
  x = re.finditer("world's", name)

print(next(x).span())''' 