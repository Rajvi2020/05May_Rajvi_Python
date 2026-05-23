mystr="this is pytHon"
str="   cdfndjfhh52558557hdsgfegegtvgfgfg     "
str3="efghrg49784787"
str2="DGDFGFDGDFGGDFGR"
num="123458555"
# #strings as array
# print(mystr[1])

# #length of string
# print(len(mystr))

# #removing extra space by strip
# print(str.strip())

# print(mystr.lower()) casefold is same as lower method
#print(str2.casefold())

# print(mystr.upper())
# print(mystr.capitalize()) capitalize is same as upper

# print(mystr.replace("pytHon","java"))
#print(mystr.replace("H","h"))

# print(mystr.split())


# age=29
# str1="my ageis {}"
# print(str1.format(age))

#print(mystr.count("p"))

#print(mystr.endswith("n")) returns true or False

#print(mystr.startswith("q"))

# print(mystr.find("p"))
# print(mystr.index("p")) find and index methods are same
#print(mystr.find("P")) returns -1 because character does not exist

#print(mystr.isalpha()) #does not include space so false

#print(num.isdigit())

#print(str3.isalnum())

#print("Center :",str.center(50))

# print("123".isdecimal())
# print("12a".isdecimal())
# print("a".isdecimal())

#print("1.1".isnumeric()) because . is not numberic so false

# print("my_var".isidentifier())
# print("2name".isidentifier())
# print("my-name".isidentifier())
"""isidentifier() check kare chhe ke string Python variable name tarike valid chhe ke nahi.
"int" valid identifier chhe because:
letters use thay chhe
koi special character nathi
number thi start thatu nathi
Etle output True."""

# print("Abs".islower())
# print("Abc".istitle())
# print("a".isupper())

#join() characters vachche given separator mukhe chhe.
# Ahiya separator chhe:
# "-"
# String "Tops" na darek character vachche - mukai jay chhe.

# text = "Hello"
# print(text.ljust(30, '*'))
# Output
# Hello*************************
# Explanation
# ljust(width, fillchar) string ne left side ma muki right side fill kare chhe.

"""text = "Hello This is Python"
print(text.partition("This"))
Output
('Hello ', 'This', ' is Python')
Explanation
partition() 3 values return kare chhe:
(before_separator, separator, after_separator)
Ahiya:
before → "Hello "
separator → "This"
after → " is Python"""

"""split()
text = "Hello world of Python"
print(text.split("o", maxsplit=3))
Output
['Hell', ' w', 'rld ', 'f Python']
Explanation
split("o")
→ jya o ave tya string ne cut kare.
maxsplit=3
→ maximum 3 vaar split karse."""

# Swapcase():
# Capital letters → small
# Small letters → CAPITAL
# Example:
#print("RaJvI".swapcase())

#print("str[-6:-1]",mystr[-6:-1]) -1 is not included


# s1 = "anjali patel"
# print(s1)
# s2 = s1.split() # by default split from space 
# print(s2)

# s3 = "python programing | java programing |flutter technology"
# s4 = s3.split("|",1)
# print(s4)

# account_no = "785412"
# print(account_no.zfill(11)) zfill() string ni left side ma 0 add kare chhe jya sudhi total length given number jetli na thai.

