import re
email = input("Enter your Gmail address: ")
#pattern = r"^[a-z].*@gmail\.com$"
x=re.match(r"^[a-z].*@gmail\.com$",email)
if x:
  print("match done")
else:
  print("not match")
# if re.match(pattern, email):
#     print("Valid Gmail")
# else:
#     print("Invalid Gmail")