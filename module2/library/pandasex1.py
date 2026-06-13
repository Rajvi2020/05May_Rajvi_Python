import pandas
stdata={
  'id':[1,2,4,5,7]
}
dt=pandas.DataFrame(stdata)
print(dt[['id']])
#print(dt)