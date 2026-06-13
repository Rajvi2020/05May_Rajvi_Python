import pandas 
import requests as r

url="https://fakestoreapi.com/products"

req=r.get(url)
data=req.json()
df=pandas.DataFrame(data)
#print(df[['id','title','price','rating']]) for multiple columns
print(df[['title']]) # to get op with heading
#print(df['title']) #to get without heading


