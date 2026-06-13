import requests
url="https://fakestoreapi.com/products/"
req=requests.get(url)
data=req.json()
print(data)

# requests.get(url) → API ને request મોકલે છે.
# req.json() → JSON data ને Python list/dictionary માં convert કરે છે.
# print(data) → બધા products બતાવે છે.
