import requests
url="https://fakestoreapi.com/products/"
req=requests.get(url)
data=req.json()
for i in data:
  print(i['id'])
  print(i['title'])


# requests.get(url) → API ને request મોકલે છે.
# req.json() → JSON data ને Python list/dictionary માં convert કરે છે.
'''for i in data → દરેક product પર loop ચલાવે છે.
i['id'] → Product ID આપે છે.
i['title'] → Product Title આપે છે.
'''