list1 = ['banana', 'apple', 'mango']

search = input("Enter fruit name to search: ")

for fruit in list1:
    if fruit == search:
        print("Fruit found in the list")
        break
else:
    print("Fruit not found in the list")