3#stdata={'id':101,'name':"rajvi",'city':'rajkot'}
#stdata={'id':102,'name':"rajvi",'city':'rajkot'}
#print(stdata)#ama 102  vali override thase

stdata={
  'id':[1,2,3,4,5],
  'name':['sanket','rajvi','kishan','dharmendra'],
  'city':['rajkot','mahuva','bhavanagar','ahmendabad','gondal']
}
print(stdata['id'])
print(stdata['id'][0])
for i,j in stdata.items():
  print(i,j[0])

#another approach for nested dictionary
# stdata=[
#   {'id':101,'name':'kishan'},
#   {'id':102,'name':'kishan'},
#   {'id':103,'name':'kishan'},
  

# ]
# print(stdata)  

#dictionary methods

stdata={'id':101,'name':"rajvi",'city':'rajkot'}
# print(stdata["name"])
# print(stdata.get("city"))
# print(stdata.keys())
# print(stdata.values())
# print(len(stdata))
if 'name' in stdata:
  print("yes")
else:
  print("no") #nmae as only key 

if 'sanket' in stdata:
  print("yes")
else:
  print("no")

'''if 'name' in stdata:
'name' key dictionary માં છે કે નહીં તે ચેક કરે છે.
જો key હોય તો "yes" print થશે.
ન હોય તો "no" print થશે.
if 'sanket' in stdata:
'sanket' ને key તરીકે શોધે છે.
Value તરીકે નથી શોધતું.
જો 'sanket' key ન હોય તો "no" print થશે.'''
 


for i in stdata.values():
  print(i)

for i ,j  in stdata.items():
  print(i,j)


for i,j in stdata.items():
  print(f"key:{i} and values:{j}")

stdata["id"]=102
print(stdata)#update a value

stdata["sub"]="python" #add a key 
print(stdata)

stdata.pop("sub")
print(stdata)

#del stdata
#print(stdata) #this will give error after del because no stdata exist now.

#del stdata["id"]
#print(stdata)

#loop through a dictionary
for x in stdata:
  print(x)

for x in stdata.values():
  print(x)

newsdata=stdata.copy()
print(newsdata)

#nested dictionary
stdata={
  'id':[1,2,3,4,5],
  'name':["l","g","e","h","q"],
  'city':['t','q','f','b'],
}
print(stdata["city"][3])

stdata=[
  {'id':101,'name':'rajvi','city':'rajkot'},
  {'id':101,'name':'rajvi','city':'rajkot'},
  {'id':101,'name':'rajvi','city':'rajkot'},
  {'id':101,'name':'rajvi','city':'rajkot'}
  
]
print(stdata[0])

for i in stdata:
  print(i)