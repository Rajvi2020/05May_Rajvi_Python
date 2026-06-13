data={}
n=int(input("enter key value pair"))
for i in range(n):
  key=input("enter key")
  value=input("enter value")
  data[key]=value
print(data)  


'''data = {}
Empty dictionary બનાવે છે.
Dictionary માં data key:value pair ના રૂપમાં store થાય છે.
n = int(input("enter key value pair"))
User પાસેથી કેટલા key-value pair દાખલ કરવાના છે તે લે છે.
for i in range(n):
n વખત loop ચલાવે છે.
key = input("enter key")
Dictionary માટે key લે છે.
value = input("enter value")
Dictionary માટે value લે છે.
data[key] = value
Dictionary માં key અને value store કરે છે.
print(data)
આખી dictionary display કરે છે.
Example

Input:

enter key value pair: 3
enter key: id
enter value: 101
enter key: name
enter value: rajvi
enter key: city
enter value: surat

Output:

{'id': '101', 'name': 'rajvi', 'city': 'surat'}'''