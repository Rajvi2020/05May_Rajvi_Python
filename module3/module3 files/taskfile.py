from datetime import datetime
f = open("data1.txt", "w")
n = int(input("Enter no of students: "))
for i in range(n):
    id = input("Enter id: ")
    name = input("Enter name: ")
    city = input("Enter city: ")
    f.write(str(datetime.now()) + "\n")
    f.write(id + "\n")
    f.write(name + "\n")
    f.write(city + "\n")
f.close()
f = open("data1.txt", "r")
while True:
    timestamp = f.readline()
    if timestamp=="":
        break
    id = f.readline()
    name = f.readline()
    city = f.readline()
    print("Timestamp:", timestamp)
    print("ID:", id)
    print("Name:", name)
    print("City:", city)
    print()
