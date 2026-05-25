#stdata={'id':101,'name':"rajvi",'city':'rajkot'}
#stdata={'id':102,'name':"rajvi",'city':'rajkot'}
#print(stdata)#ama 102  vali override thase

stdata={
  'id':[1,2,3,4,5],
  'name':['sanket','rajvi','kishan','dharmendra'],
  'city':['rajkot','mahuva','bhavanagar','ahmendabad','gondal']
}
# print(stdata['id'])
# print(stdata['id'][0])
# for i,j in stdata.items():
#   print(i,j[0])

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


